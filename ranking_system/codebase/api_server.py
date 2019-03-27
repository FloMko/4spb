# -*- coding: utf-8 -*-
from flask import request, url_for
#from flask_cors import CORS
from flask_api import FlaskAPI, status, exceptions
import json
import db_helper

mongourl = 'mongodb://root:rootPassXXX@127.0.0.1:27017/admin'
database = 'lostpets'
collection = 'dataset'


app = FlaskAPI(__name__)
db = db_helper.db(mongourl,database,collection)


@app.route('/search/',methods=['POST'])
def search():
    '''
    didn't worked yet
    '''
    search_list = list()
    data = request.get_json()
    response = db.search_records(data)
    for res in response:
        search_list.append(res)
    return str(search_list)


@app.route('/populate/',methods=['POST'])
def insert():
    '''
    Get POST json. populate db
    '''
    data = request.get_json()
    # data_new = db.read_request(data)
    res = db.write_record(data)
    return str(res)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
