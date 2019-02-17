# -*- coding: utf-8 -*-
from flask import request, url_for
#from flask_cors import CORS
from flask_api import FlaskAPI, status, exceptions
import json
import db_helper

app = FlaskAPI(__name__)


@app.route('/search/',methods=['POST'])
def search():
    '''
    didn't worked yet
    '''
    search_list = list()
    print("searched data : {}".format(request.get_json()))
    data = request.get_json()
    response = db_helper.search_record(data)
    for res in response:
        if res['response']:
            print(res['response'])
            search_list.append(res['response'])
            print("one:",res)
    print(search_list)
    return search_list


@app.route('/populate/',methods=['POST'])
def insert():
    '''
    Get POST json. populate db
    '''
    print("Posted data : {}".format(request.get_json()))
    data = request.get_json()
    print(data)
    data_new = db_helper.read_request(data)
    res = db_helper.write_record(data_new)
    return str(res)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
