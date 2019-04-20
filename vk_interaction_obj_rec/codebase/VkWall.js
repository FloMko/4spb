const vk = require('vk-easy');
require('dotenv').load();
const axios = require('axios');
const _ = require('underscore');
var url = 'http://api-python:5000' // url базы данных Максима
var BOT_TOKEN = process.env.BOT_TOKEN
var DATA = {}


function getWall() {
  vk('wall.get', {
    access_token: BOT_TOKEN,
    domain: 'yapoteryalsyaspb',
    count: 50,
  }, true).then(res => {
    sendToDb(res)
  });
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


getWall()

