const vk = require('vk-easy');
require('dotenv').load();
const axios = require('axios');
const _ = require('underscore');
var url = process.env.API_URL // url базы данных Максима
var BOT_TOKEN = process.env.BOT_TOKEN


function getWall() {
  vk('wall.get', {
    access_token: BOT_TOKEN,
    domain: 'yapoteryalsyaspb',
    count: 50,
  }, true).then(async res => {
    
    try {
      const margin = await getLatestDate()

      for (let wallPost of res.response.items) {
        if (wallPost.date > margin) {
          sendToDb(wallPost)
        } else {
          console.log(`post ${wallPost.id} already exists`)
        }
      }
    } catch(err) {
      console.log(err)
    }

  });
}


function sendToDb(data) {
  axios.post(`${url}/populate/`, data)
    .then(response =>
      console.log(`${data.id} – ${response.status}`))
    .catch(err => console.log(err));
}


function getLatestDate() {
  return axios.get(`${url}/get_latest`)
    .then(response => response.data)
    .catch(err => 0)
}


getWall()
