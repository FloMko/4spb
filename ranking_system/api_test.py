import requests
import ast

# functional module
import codebase.db_helper as db_helper

# use logging
import logging
# let's test
import unittest


# images_url = 'http://127.0.0.1:5000/find_image/'
# res = requests.post(images_url, json={'photo': 'https://sun9-12.userapi.com/c850232/v850232199/122ff9/LYV4oeT3L3U.jpg'})
# data = ast.literal_eval(res.text)


class ApiTest(unittest.TestCase):
    """
    check api smoke tests
    """

    # def __init__(self):
    #     self.api_find_image_url = 'http://127.0.0.1:5000/find_image/'

    def test_old_database_init(self, ):
        """check connection to db"""
        print("id: " + self.id())
        mongourl = 'mongodb://root:rootPassXXX@127.0.0.1:27017/admin'
        database = 'lostpets'
        collection = 'dataset'
        old_db = db_helper.Db(mongourl, database, collection)
        self.assertIsInstance(
            old_db.search_record({}),
            dict)

    def test_new_database_init(self, ):
        """check connection to db"""
        print("id: " + self.id())
        mongourl = 'mongodb://root:rootPassXXX@127.0.0.1:27017/admin'
        database = 'lostpets'
        collection_new = 'datastore'
        new_db = db_helper.Db(mongourl, database, collection_new)
        self.assertIsInstance(
            new_db.search_record({}),
            dict)

    def test_init_api(self, ):
        """ return right status code"""
        print("id: " + self.id())
        try:
            self.assertEqual(
                requests.post('http://127.0.0.1:5000/find_image/',
                              'https://sun9-12.userapi.com/c850232/v850232199/122ff9/LYV4oeT3L3U.jpg').status_code,
                500)
        except ConnectionError:
            logging.debug('error connect')
        pass


if __name__ == '__main__':
    # logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()
