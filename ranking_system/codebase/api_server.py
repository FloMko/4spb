# -*- coding: utf-8 -*-
from flask import request
from flask_api import FlaskAPI
from bson import json_util
import db_helper
import vectorize as vectorize
import image_helper as imagehelper
import cluster as cluster




class Api():
    """
    class for rest interaction
    """
    def __init__(self):
        mongourl = 'mongodb://root:rootPassXXX@127.0.0.1:27017/admin'
        database = 'lostpets'
        collection = 'dataset'
        collection_new = 'datastore'
        self.dataset_path = '../dataset/'
        self.cluster = cluster.Cluster()
        self.vec = vectorize.Vectors()
        self.db = db_helper.Db(mongourl, database, collection)
        self.db_new = db_helper.Db(mongourl, database, collection_new)
        self.app = FlaskAPI(__name__)
        self.app.add_url_rule("/search/","search", self.search, methods=['POST'])
        self.app.add_url_rule("/populate/","populate", self.insert, methods=['POST'])
        self.app.add_url_rule("/search_trans/","search_trans", self.search_trans, methods=['POST'])
        self.app.add_url_rule("/populate_trans/","populate_trans", self.insert_trans, methods=['POST'])
        self.app.add_url_rule("/find_image/","find_image", self.find_image, methods=['POST'])
        self.app.add_url_rule("/load_knn/", "load_cluster", self.load_cluster, methods=['POST'])
        print("init api")


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

    def find_image(self):
        """
        get json with 'photo' : %photo_name%
        :return: search results
        https://pp.userapi.com/c851216/v851216826/efbc4/pnz7eaWD3b8.jpg
        """
        response = []
        self.cluster.load()
        data = request.get_json()
        print(data['photo'])
        imhelp = imagehelper.Helper(dataset_path='../tmpdata/')
        path = imhelp.download_image(photo_url=data['photo'])
        imhelp.resize(path)
        vect = self.vec.get_vector(path)
        dist, indices = self.cluster.find_nearest(vect)
        images = imagehelper.Helper(self.dataset_path).get_images()
        near = self.cluster.get_similar_images(images, dist,indices)
        for photo in near[:5]:
            response.append(self.db_new.search_records({'photos_name':{'$elemMatch':{'$in':[data['photo']]}}}))
        return json_util.dumps(response)

    def load_cluster(self):
        self.cluster.load()
        return "cluster loaded"

if __name__ == "__main__":
    api = Api()
    api.app.run(host='0.0.0.0', debug=True)
