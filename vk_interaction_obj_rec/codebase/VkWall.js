const vk = require('vk-easy');
require('dotenv').load();
const natural = require('natural');
const ndarray = require('ndarray');
const ops = require('ndarray-ops');
const axios = require('axios');
const KerasJS = require('keras-js')
var jpeg = require('jpeg-js');
var getPixels = require("get-pixels")
var IN = require("./imageNetClasses.js")
const _ = require('underscore');
const { Image, createCanvas, loadImage } = require('canvas')
//
var url = 'http://127.0.0.1:5000' // url базы данных Максима
var BOT_TOKEN = process.env.BOT_TOKEN
var DATA = {}


function getWall() {
  vk('wall.get', {
    access_token: BOT_TOKEN,
    domain: 'yapoteryalsyaspb',
    count: 100,
  }, true).then(res => {
    sendToDb(res)
  });
}


function getWallAndFindText() {
  vk('wall.get', {
    access_token: BOT_TOKEN,
    domain: 'yapoteryalsyaspb',
    count: 100,
  }, true).then(res => {
    console.log(useText(res.response.items));
  });
}


function useText(arr) {
  var res = {}
  var tokenizer = new natural.AggressiveTokenizerRu();
  arr.map((item, i) => {
    var words = tokenizer.tokenize(arr[i].text)
    // console.log(words);
    var isLost = 0
    var isFound = 0
    words.map((item, i) => {
      if (same(item, 'пропал') > 0.8 || same(item, 'потерялся') > 0.8) {
        isLost++
      } else if (same(item, 'найден') > 0.8 || same(item, 'найдена') > 0.8) {
        isFound++
      }
    })
    //
    var status = 'пропал'
    if (isFound > isLost ) {
      status = 'найден'
    } else if ( isFound === isLost ) {
      status = 'оффтоп (или дома)'
    }
    if (!res[status]) { res[status] = [] }
    res[status].push(item)
  })
  return res
}



function sendToDb(data) {
  axios.post(url+'/populate/', data)
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });
}



function findInDb(data) {
  axios.post(url+'/search/', {})
  .then(function (response) {
    console.log(response.data);
  })
  .catch(function (error) {
    console.log(error);
  });
}



async function getImage() {
  vk('wall.get', {
    access_token: BOT_TOKEN,
    domain: 'yapoteryalsyaspb',
    count: 10,
  }, true).then( async (res) => {
    var url = res.response.items[3].attachments[0].photo.photo_604
    // console.log(res.response.items[1].attachments[0]);
    console.log(url);
    var h = 224, w = 224
    const canvas = createCanvas(w, h)
    const ctx = canvas.getContext('2d')
    const myimg = await loadImage(url)
    // console.log(myimg);
    ctx.drawImage(myimg, 0, 0, 448, 224);
    var pixel = ctx.getImageData(0, 0, w, h);
    pixel.width = w
    pixel.height = h
    // var data = await imageDataToPixels(pixel.data,w)
    var data = preprocess(pixel)
    // console.log(data);
    useModel(data)
  });
}



function useModel(data) {
  // console.log('data in model',data);
  const model = new KerasJS.Model({
    filepath: './data/resnet50.bin',
    filesystem: true
  })
  //
  model
  .ready()
  .then(() => {
    console.log('keras is ready');
    // input data object keyed by names of the input layers
    // or `input` for Sequential models
    // values are the flattened Float32Array data
    // (input tensor shapes are specified in the model config)
    const inputData = {
      input_1: data
    }
    // make predictions
    return model.predict(inputData)
  })
  .then(outputData => {
    var res = {}
    var array = Array.from(outputData['fc1000']);
    // console.log(array);
    for (var i = 0; i < array.length; i++) {
      var imNet = IN.IMAGENET[i][1]
      var item = {}
      item[imNet] = outputData['fc1000'][i]
      res[i] = item
    }
    // console.log(res);
    var resBy = {}
    for (var i = 0; i < array.length; i++) {
      var out = outputData['fc1000'][i]
      var imNet = IN.IMAGENET[i][1]
      var item = {}
      item[out] = imNet
      if (out > 0.01) {
        resBy[i] = item
      }
    }
    console.log(resBy);
    // outputData is an object keyed by names of the output layers
    // or `output` for Sequential models
    // e.g.,
    // outputData['fc1000']
  })
  .catch(err => {
    console.log(err);
    // handle error
  })
}



function imageDataToPixels(data, w) {
  var arr = []
  data.map((item,i) => {
    arr[i] = (data[i] / 255 - 0.5) * 2
    // arr[i] = data[i] / 255
  })
  // var res0 = _.chunk(data, 1);
  var res1 = _.chunk(arr, 4);
  res1.map((item,i) => {
    res1[i].pop()
  })
  var res2 = _.chunk(res1, w);
  // var res3 = _.chunk(res2, w);
  return res2;
}



getWall()
// findInDb()
// useModel()
// getImage()
// getWallAndFindText()


///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////



function same(w1, w2) {
  return natural.DiceCoefficient(w1, w2)
}


function preprocess(imageData) {
  const { data, width, height } = imageData
  // data processing
  // see https://github.com/keras-team/keras/blob/master/keras/applications/imagenet_utils.py
  const dataTensor = ndarray(new Float32Array(data), [width, height, 4])
  const dataProcessedTensor = ndarray(new Float32Array(width * height * 3), [width, height, 3])
  ops.subseq(dataTensor.pick(null, null, 2), 103.939)
  ops.subseq(dataTensor.pick(null, null, 1), 116.779)
  ops.subseq(dataTensor.pick(null, null, 0), 123.68)
  ops.assign(dataProcessedTensor.pick(null, null, 0), dataTensor.pick(null, null, 2))
  ops.assign(dataProcessedTensor.pick(null, null, 1), dataTensor.pick(null, null, 1))
  ops.assign(dataProcessedTensor.pick(null, null, 2), dataTensor.pick(null, null, 0))
  const preprocessedData = dataProcessedTensor.data
  return preprocessedData
}
///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
