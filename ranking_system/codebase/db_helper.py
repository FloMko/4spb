import pymongo

class Db():
    def __init__(self, mongourl, database, collection):
        self.client = pymongo.mongo_client.MongoClient(mongourl)
        self.db = self.client[database]
        self.collection = self.db[collection]

    def write(self, reg):
        """
        for input info from flask
        :param reg: request from outer side
        :return: count of total writes
        """
        inserted_count = 0
        for data in reg:
            response = self.write_record(data['response'])
            inserted_count += response

    def write_record(self, formatted_req):
        """
        :param formatted_req: bson to db
        :return: response from db with count
        """
        req = [pymongo.InsertOne(formatted_req)]
        res = self.collection.bulk_write(req)
        return res.inserted_count

    def search_records(self, search_req):
        """
        :param search_req: search for record
        :param search_req:
        :return:
        """
        res = self.collection.find(search_req)
        return res

    def search_formatted_record(self, search_req):
        """
        :param search_req: search for record
        :return: all of them
        """
        unformatted = self.collection.find(search_req)
        result = []
        for form in unformatted:
            result.append(form)
        return result
