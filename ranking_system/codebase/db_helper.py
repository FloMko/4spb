import pymongo


class Db:
    def __init__(self, mongourl, database, collection):
        self.client = pymongo.mongo_client.MongoClient(mongourl)
        self.db = self.client[database]
        self.collection = self.db[collection]

    def read_request(self, json_req):
        # Get json data, convert to mongo insert
        return json_req

    def write(self, reg):
        inserted_count = 0
        for data in reg:
            response = self.write_record(data["response"])
            inserted_count += response

    def write_record(self, formatted_req):
        # write bson to db, return res
        req = [pymongo.InsertOne(formatted_req)]
        res = self.collection.bulk_write(req)
        return res.inserted_count

    def search_record(self, search_req):
        # return result from spec collection
        res = self.collection.find_one(search_req)
        return res

    def search_latest_record(self):
        # return latest result from spec collection
        res = self.collection.find_one({}, sort=[("date", pymongo.DESCENDING)])
        return res

    def search_records(self, search_req):
        # return result from spec collection
        res = self.collection.find(search_req)
        return res
