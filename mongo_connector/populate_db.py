import pymongo
from bson import json_util
import json



def connect():
    client =  pymongo.mongo_client.MongoClient('mongodb://root:rootPassXXX@localhost:27017/admin')
    db = client.db.admin
    return db

def 


req = [pymongo.InsertOne({'y': 1})]
res = db.test.bulk_write(req1)


db = connection.database
posts = db.posts
post_id = posts.insert_many(data).inserted_id