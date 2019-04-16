import requests

# import codebase.find_helper as findhelper

# use logging
import logging

# get config
import yaml

cfg = yaml.safe_load(open("../codebase/config.yaml"))

api_url = cfg['api_url']
image_url = cfg['image_url']


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
