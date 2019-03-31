# -*- coding: utf-8 -*-
from flask import request
from flask_api import FlaskAPI
from bson import json_util
import db_helper


mongourl = 'mongodb://root:rootPassXXX@127.0.0.1:27017/admin'
database = 'lostpets'
collection = 'dataset'
collection_new= 'datastore'


app = FlaskAPI(__name__)
db = db_helper.Db(mongourl,database,collection)
db_new = db_helper.Db(mongourl,database,collection_new)


@app.route('/search/',methods=['POST'])
def search():
    """
    get request, search in db for data
    """
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

@app.route('/find_image/', methods=['POST'])
def find_image_trans():
    """
    get json with 'photo' : %photo_name%
    :return: search results
    """
    data = request.get_json()
    response = db_new.search_records({'photos_name':{'$elemMatch':{'$in':[data['photo']]}}})
    return json_util.dumps(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
