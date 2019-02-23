var natural = require('natural');

var text = `Вовсе нет. Это означает, что мы еще в самом начале пути. 10-15 лет назад, когда приложения начали захватывать мир, доводы в их пользу были очевидными. Было просто быстрее и удобнее использовать для многих целей приложение, чем делать это через мобильные веб-сайты.

Сегодня чат-боты не имеют тех же самых преимуществ – скорости и эффективности – по сравнению с мобильным интернетом. Но даже когда это изменится, из-за недостатка точности я не смогу быть уверен в том, что чат-бот сможет выполнить свою задачу правильно.`


var WordTokenizer = new natural.AggressiveTokenizerRu();
var SentenceTokenizer = new natural.SentenceTokenizer();
var allWords = WordTokenizer.tokenize(text)
var allSents = SentenceTokenizer.tokenize(text)

// подсчет количества повторяющихся слов
var couWords = {};
allWords.forEach((word) => { couWords[word] = (couWords[word] || 0) + 1; });

// подсчет количчества похожих (не обязательно однородных) слов
var couSimWords = {}
allWords.forEach((word1) => {
  allWords.forEach((word2) => {
    if (natural.DiceCoefficient(word1, word2)>0.7) {
      couSimWords[word1] = (couSimWords[word1] || 0) + 1;
    }
  });
});

// перевод слова в вектор по буквам
function word2vec(word) {
  var chars = word.split('');
  var wordVec = new Array(30).fill(0);
  chars.map((char,i) => {
    wordVec[i] = char.charCodeAt(0)-1040;
  })
  return wordVec
}


///////////////////////////////////////////////
///////////////////////////////////////////////
///////////////////////////////////////////////
var tf = require('@tensorflow/tfjs-node');

/*
// net building
const model = tf.sequential();
model.add(tf.layers.dense({
  inputShape: [4], // size of input data
  units: 2,  // size of output data
  activation: 'sigmoid',
}));
model.compile({
  loss: 'meanSquaredError',
  optimizer: tf.train.adam(0.06),
  // optimizer: 'sgd',
});


// training
var trainData = tf.tensor2d([0, 0, 0, 1],[1,4])
var outputData = tf.tensor2d([0, 1],[1,2])
var testData = tf.tensor2d([0, 0, 0, 1],[1,4])
//
model.fit(trainData, outputData, {epochs: 100}).then(() => {
  // Use the model to do inference on a data point the model hasn't seen before:
  model.predict(testData).print();
  // Open the browser devtools to see the output
});
*/


/*
const image = new ImageData(1, 1);
image.data[0] = 100;
image.data[1] = 150;
image.data[2] = 200;
image.data[3] = 255;
tf.fromPixels(image).print();
*/




// Define a model for linear regression.
/*
const model = tf.sequential();
model.add(tf.layers.dense({
  units: 1,
  inputShape: [1]
}));

model.compile({
  loss: 'meanSquaredError',
  optimizer: 'sgd',
});

// Generate some synthetic data for training.
const inpData = tf.tensor2d([1, 2, 3, 4], [4, 1]);
const outpData = tf.tensor2d([1, 3, 5, 7], [4, 1]);

// Train the model using the data.
model.fit(inpData, outpData, {epochs: 100}).then(() => {
  // Use the model to do inference on a data point the model hasn't seen before:
  var testData = tf.tensor2d([1, 2, 3, 4], [4, 1])
  model.predict(testData).print();
  // Open the browser devtools to see the output
});
*/




// net building
const model = tf.sequential({
   layers: [
     tf.layers.dense({inputShape: [30], units: 10, activation: 'relu'}),
     tf.layers.dense({inputShape: [10], units: 1, activation: 'relu'}),
   ]
});
model.compile({
  loss: 'meanSquaredError',
  optimizer: tf.train.adam(0.02),
  // optimizer: 'sgd',
});


// data
var wordVecTensor = []
allWords.map((word,i) => {
  var res = word2vec(word)
  wordVecTensor.push(res)
})
var wordLenTensor = []
allWords.map((word,i) => {
  var res = word.length
  wordLenTensor.push([res])
})
// console.log(wordVecTensor);


var trainData = tf.tensor2d(wordVecTensor)
var outputData = tf.tensor2d(wordLenTensor)
var num = 3
var testData = tf.tensor2d([wordVecTensor[num]])
// var trainData = tf.tensor2d([[0, 0], [0, 1]])
// var outputData = tf.tensor2d([[0], [1]])
// var testData = tf.tensor2d([[0, 0]])


// training
var config = {
  epochs: 100,
  shuffle: true,
}

model.fit(trainData, outputData, config).then(() => {
  // Use the model to do inference on a data point the model hasn't seen before:
  model.predict(testData).print();
  console.log('len ',wordLenTensor[num]);
  // Open the browser devtools to see the output
});
