const vk = require('vk-easy')
require('dotenv').load()
const axios = require('axios')
const cron = require('cron')
var url = process.env.API_URL
var BOT_TOKEN = process.env.BOT_TOKEN


function getWall() {
  vk('wall.get', {
    access_token: BOT_TOKEN,
    domain: 'yapoteryalsyaspb',
    count: 50,
  }, true).then(async res => {
    
    try {
      const margin = await getLatestDate()

      let skippedCount = 0
      for (let wallPost of res.response.items) {
        if (wallPost.date > margin) {
          sendToDb(wallPost)
        } else {
          skippedCount++
        }
      }

      console.log(`${skippedCount} out of ${res.response.items.length} posts already exist`)
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


const updateMinutes = 5
console.log(`Updating at every ${updateMinutes}th minute`)
new cron.CronJob(`*/${updateMinutes} * * * *`, () => {
  console.log('Scraping wall')
  getWall()
}, null, true)
