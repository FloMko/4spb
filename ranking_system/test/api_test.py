import requests

# import codebase.find_helper as findhelper

# use logging
import logging

# let's test

api_url = 'http://ec2-34-245-226-15.eu-west-1.compute.amazonaws.com:5000'
image_url = 'https://pp.userapi.com/c851216/v851216826/efbc4/pnz7eaWD3b8.jpg'


def test_init_api_search():
    """ check connection through api to db"""
    try:
        assert requests.post(api_url + '/search_trans/', json={}).status_code == 200
    except ConnectionResetError:
        logging.debug('error connect')
    pass


def test_api():
    """ return right res"""
    isinstance(
        requests.post(api_url + '/find_image/', json={'photo': image_url}),
        requests.models.Response)


def test_init_api():
    """ return right status code"""
    request_url = api_url + '/find_image/'
    assert requests.post(request_url, json={'photo': image_url}).status_code == 200
