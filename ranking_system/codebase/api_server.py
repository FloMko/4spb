# -*- coding: utf-8 -*-
from flask import request, Response
#from flask_cors import CORS
from flask_api import FlaskAPI, status, exceptions
from bson import json_util, ObjectId
import db_helper


mongourl = 'mongodb://root:rootPassXXX@127.0.0.1:27017/admin'
database = 'lostpets'
collection = 'dataset'
collection_new= 'datastore'


app = FlaskAPI(__name__)
db = db_helper.db(mongourl,database,collection)
db_new = db_helper.db(mongourl,database,collection_new)


@app.route('/search/',methods=['POST'])
def search():
    """
    get request, search in db for data
    """
    search_list = list()
    data = request.get_json()
    response = db.search_records(data)
    return json_util.dumps(response)

@app.route('/populate/',methods=['POST'])
def insert():
    """
    Get POST json. populate db
    """
    data = request.get_json()
    # data_new = db.read_request(data)
    res = db.write_record(data)
    return str(res)

@app.route('/search_trans/',methods=['POST'])
def search_trans():
    """
    get request, search in db for data
    """
    search_list = list()
    data = request.get_json()
    response = db_new.search_records(data)
    return json_util.dumps(response)

@app.route('/populate_trans/',methods=['POST'])
def insert_trans():
    """
    Get POST json. populate db
    """
    data = request.get_json()
    # data_new = db.read_request(data)
    res = db_new.write_record(data)
    return str(res)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
