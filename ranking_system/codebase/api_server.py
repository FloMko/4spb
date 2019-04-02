# -*- coding: utf-8 -*-
from flask import request
from flask_api import FlaskAPI
from bson import json_util
import db_helper


class Api():
    """
    class for rest interaction
    """
    def __init__(self):
        mongourl = 'mongodb://root:rootPassXXX@127.0.0.1:27017/admin'
        database = 'lostpets'
        collection = 'dataset'
        collection_new = 'datastore'
        self.db = db_helper.Db(mongourl, database, collection)
        self.db_new = db_helper.Db(mongourl, database, collection_new)
        self.app = FlaskAPI(__name__)
        self.app.add_url_rule("/search/","search", self.search, methods=['POST'])
        self.app.add_url_rule("/populate/","populate", self.insert, methods=['POST'])
        self.app.add_url_rule("/search_trans/","search_trans", self.search_trans, methods=['POST'])
        self.app.add_url_rule("/populate_trans/","populate_trans", self.insert_trans, methods=['POST'])
        self.app.add_url_rule("/find_image/","find_image", self.find_image_trans, methods=['POST'])


    def search(self):
        """
        get request, search in db for data
        """
        data = request.get_json()
        response = self.db.search_records(data)
        return json_util.dumps(response)

    def insert(self):
        """
        Get POST json. populate db
        """
        data = request.get_json()
        # data_new = db.read_request(data)
        res = self.db.write_record(data)
        return str(res)

    def search_trans(self):
        """
        get request, search in db for data
        """
        data = request.get_json()
        response = self.db_new.search_records(data)
        return json_util.dumps(response)

    def insert_trans(self):
        """
        Get POST json. populate db
        """
        data = request.get_json()
        res = self.db_new.write_record(data)
        return str(res)

    def find_image_trans(self):
        """
        get json with 'photo' : %photo_name%
        :return: search results
        """
        data = request.get_json()
        response = self.db_new.search_records({'photos_name':{'$elemMatch':{'$in':[data['photo']]}}})
        return json_util.dumps(response)





if __name__ == "__main__":
    api = Api()
    api.app.run(host='0.0.0.0', debug=True)
