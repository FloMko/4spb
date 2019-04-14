import requests
import ast

# functional module
import codebase.db_helper as db_helper
# import codebase.find_helper as findhelper

# use logging
import logging
# let's test
import unittest


class ApiTest(unittest.TestCase):
    """
    check api smoke tests
    """

    # def __init__(self):
    #     self.api_find_image_url = 'http://127.0.0.1:5000/find_image/'
    # @classmethod
    # def setUpClass(cls):
    #     """Set up for class"""
    #     api_server_url = 'https://instar.serveo.net'
    #     image_url = 'https://pp.userapi.com/c851216/v851216826/efbc4/pnz7eaWD3b8.jpg'
    #     response = requests.post(
    #         api_server_url + '/find_image/',
    #         json={'photo': image_url})



    def test_old_database_init(self, ):
        """check connection to old db"""
        print("id: " + self.id())
        mongourl = 'mongodb://root:rootPassXXX@127.0.0.1:27017/admin'
        database = 'lostpets'
        collection = 'dataset'
        old_db = db_helper.Db(mongourl, database, collection)
        self.assertIsInstance(
            old_db.search_record({}),
            dict)

    def test_new_database_init(self, ):
        """check connection to new db"""
        print("id: " + self.id())
        mongourl = 'mongodb://root:rootPassXXX@127.0.0.1:27017/admin'
        database = 'lostpets'
        collection_new = 'datastore'
        new_db = db_helper.Db(mongourl, database, collection_new)
        self.assertIsInstance(
            new_db.search_record({}),
            dict)

    def test_init_api_search(self, ):
        """ check connection through api to db"""
        print("id: " + self.id())
        try:
            self.assertEqual(
                requests.post('http://ec2-34-245-226-15.eu-west-1.compute.amazonaws.com:5000/search_trans/', json={}).status_code,
                200)
        except ConnectionResetError:
            logging.debug('error connect')
        pass

    def test_api(self, ):
        """ return right res"""
        print("id: " + self.id())
        images_url = 'http://ec2-34-245-226-15.eu-west-1.compute.amazonaws.com:5000/find_image/'
        self.assertIsInstance(
            requests.post(
                images_url,
                json={'photo': 'http://pp.userapi.com/c851216/v851216826/efbc4/pnz7eaWD3b8.jpg'}),
        requests.models.Response)

    def test_init_api(self, ):
        """ return right status code"""
        print("id: " + self.id())
        images_url = 'http://ec2-34-245-226-15.eu-west-1.compute.amazonaws.com:5000/find_image/'
        self.assertEqual(
            requests.post(
                images_url,
                json={'photo': 'http://pp.userapi.com/c851216/v851216826/efbc4/pnz7eaWD3b8.jpg'}).status_code,
            200)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()
