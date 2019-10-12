const vk = require('vk-easy')
require('dotenv').load()
const axios = require('axios')
var url = 'http://api-python:5000' // url базы данных Максима
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
  .then(function (response) {
    console.log(`${data.id} – ${response.status}`)
  })
  .catch(function (error) {
    console.log(error);
  });
}


function getLatestDate() {
  return axios.get(`${url}/get_latest`)
  .then((response) => {
    return response.data
  })
  .catch((err) => 0)
}


getWall()
