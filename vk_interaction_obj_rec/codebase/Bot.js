const express = require('express');
require('dotenv').load();
const bodyParser = require('body-parser');
const _ = require('underscore');
const vk = require('vk-easy');
var PF = require('./Profile.js');
var BOT_TOKEN = process.env.BOT_TOKEN
var COLORS_DOG = PF.PROFILE['Цвет']['Собака']
var COLORS_CAT = PF.PROFILE['Цвет']['Кошка']


const port = 3000;
const app = express();
app.use(bodyParser.json());
app.listen(port, () => {
  console.log(`Express server is listening on ${port}`);
});
// регисстрация сервера на вк
app.post('/', (req, res) => {
  if (req.body.type == 'confirmation') {
    return res.send('f7e2e6ba');
  } else if (req.body.type == 'message_new') {
    var RESULT = {}
    dialog(req)
  }
  res.sendStatus(200);
});



function dialog(req) {
  let { body } = req
  let id = body.object.user_id

  function answer2() {
    sendMessage(id, 'Как давно потерялся?',setKeyboard(['1 месяц','2 месяца', '3 месяца']))
  }

  function answer3() {
    if (RESULT['pet'] === 'dog') {
      sendMessage(id, 'Какой размер питомца?',setKeyboard(['Маленький','Средний', 'Большой']))
    } else {
      sendMessage(id, 'Какой цвет шерсти?',setKeyboard(COLORS_CAT))
    }
  }

  function answer4() {
    sendMessage(id, 'Какой цвет шерсти?',setKeyboard(COLORS_DOG))
  }


  switch(body.object.body) {
    // 1 вопрос
    case 'Собака':
      addToResult('pet','dog')
      answer2()
      break
    case 'Щенок':
      addToResult('pet','puppy')
      answer2()
      break
    case 'Кошка':
      addToResult('pet','cat')
      answer2()
      break
    case 'Котенок':
      addToResult('pet','kitty')
      answer2()
      break

    // 2 вопрос
    case '1 месяц':
      addToResult('long','30')
      answer3()
      break
    case '2 месяца':
      addToResult('long','60')
      answer3()
      break
    case '3 месяца':
      addToResult('long','90')
      answer3()
      break

    // 3 вопрос
    case 'Маленький':
      addToResult('size','little')
      answer4()
      break
    case 'Средний':
      addToResult('long','middle')
      answer4()
      break
    case 'Большой':
      addToResult('long','big')
      answer4()
      break

    // 4 вопрос
    case 'Белая':
      addToResult('color','white')
      answer4()
      break
    case 'Черная':
      addToResult('color','black')
      answer4()
      break
    case 'Бежевая':
      addToResult('color','beuge')
      answer4()
      break
    case 'Рыжая':
      addToResult('color','red')
      answer4()
      break
    case 'Коричневая':
      addToResult('color','brown')
      answer4()
      break
    case 'Серая':
      addToResult('color','grey')
      answer4()
      break
    case 'Двухцветная':
      addToResult('color','2color')
      answer4()
      break
    case 'Трехцветная':
      addToResult('color','3color')
      answer4()
      break
    case 'Маркиз (ч/б)':
      addToResult('color','blackWhite')
      answer4()
      break
    case 'Полосатая':
      addToResult('color','striped')
      answer4()
      break
    case 'Дымчатая':
      addToResult('color','smoke')
      answer4()
      break

    // 5 вопрос про шерсть
    case 'Короткая':
      addToResult('fur','short')
      answer5()
      break
    case 'Длинная':
      addToResult('fur','long')
      answer5()
      break


    // 5 вопрос про шерсть
    case 'Прямая':
      addToResult('fur','straight')
      answer6()
      break
    case 'Кучерявая':
      addToResult('fur','curly')
      answer6()
      break


    // 6 вопрос про уши
    case 'Стоячие':
      addToResult('ears','standing')
      answer7()
      break
    case 'Висячие':
      addToResult('ears','hanging')
      answer7()
      break
    case 'Отсутствуют':
      addToResult('ears','none')
      answer7()
      break
    case 'Оба':
      addToResult('ears','both')
      answer7()
      break
    case 'Одно купировано':
      addToResult('ears','cropped')
      answer7()
      break


    // 7 вопрос про хвост
    case 'Длинный':
      addToResult('tail','long')
      answer8()
      break
    case 'Короткий':
      addToResult('tail','short')
      answer8()
      break
    case 'Отсутствует':
      addToResult('tail','none')
      answer8()
      break
    case 'Пушистый':
      addToResult('tail','bushyFur')
      answer8()
      break
    case 'Короткошерстный':
      addToResult('tail','shortFur')
      answer8()
      break
    case 'Прямой':
      addToResult('tail','straight')
      answer8()
      break
    case 'Колечком':
      addToResult('tail','ring')
      answer8()
      break


    //
    default:
      RESULT = {}
      sendMessage(id, 'Кого Вы ищете?',setKeyboard(['Собака','Щенок','Кошка','Котенок']))
      break
  }

}



function addToResult(key, t) {
  RESULT[key] = t
}


function sendMessage(id,t,kb) {
  vk('messages.send', {
    access_token: BOT_TOKEN,
    user_id: id,
    message: t,
    keyboard: JSON.stringify(kb)
  }).then(console.log);
}


function setKeyboard(arr) {
  var res = {
    "one_time": false,
    "buttons": [[]]
  }

  arr.map((item,i) => {
    res['buttons'][0].push({
      "action": {
        "type": "text",
        "payload": "{\"button\": \""+i+"\"}",
        "label": item
      },
      "color": "default"
    })
  })

  return res
}




function parseDialog(o) {
  var i1 = 0
  var i2 = 0
  for (var key1 in o) {
    if ( !Array.isArray(o[key1]) ) { // если объект
      for (var key2 in o[key1]) {
        if ( _.indexOf(o['Питомец'], key2) ) {
          // если есть разграничение по питомцам
          // выдаем вопрос
        } else {
          // если просто еще один уровень вложенности
        }
      }
    } else { // если просто список
      for (var i = 0; i < o[key1].length; i++) {
        // выдаем вопрос с кнопками
      }
    }
    i1++
  }
}
