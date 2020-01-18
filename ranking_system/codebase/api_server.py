# -*- coding: utf-8 -*-
from flask import request
from flask_api import FlaskAPI
from bson import json_util

# logging
import traceback
import logging

# get config
import yaml

# external modules
from . import dbHelper as dbHelper
from . import findHelper as findHelper
from .import main as core


cfg = yaml.safe_load(open("config.yaml"))
mongourl = cfg["mongourl"]
database = cfg["database"]
collection = cfg["collection"]
collection_new = cfg["collection_new"]
db = dbHelper.Db(mongourl, database, collection)
db_new = dbHelper.Db(mongourl, database, collection_new)
find = findHelper.Find()
app = FlaskAPI(__name__)

def search_latest():
    """
    get request, search in db for latest record
    """
    response = db.search_latest_record()
    return json_util.dumps(response["date"])


def search():
    """
    get request, search in db for data
    """
    data = request.get_json()
    response = db.search_records(data)
    return json_util.dumps(response)

def insert():
    """
    Get POST json. populate db
    """
    data = request.get_json()
    logging.debug(data)
    res = db.write_record(data)
    return str(res)

def search_trans():
    """
    get request, search in db for data
    """
    data = request.get_json()
    response = db_new.search_records(data)
    return json_util.dumps(response)

def insert_trans():
    """
    Get POST json. populate db
    """
    data = request.get_json()
    res = db_new.write_record(data)
    return str(res)

def find_image():
    """
    get json with 'photo' : %photo_name%
    :return: search results
    https://pp.userapi.com/c851216/v851216826/efbc4/pnz7eaWD3b8.jpg
    db_new.search_record({'photos_name':{'$elemMatch':{'$in':['pnz7eaWD3b8.jpg']}}})
    """
    try:
        data = request.get_json()
        logging.debug(data)
        response = find.main(data["photo"])
        return json_util.dumps(response)
    except Exception:
        logging.error(traceback.format_exc())

def update_cluster():
    """
    invoce by get
    :return: status
    """
    lastdate = db.search_latest_record()
    core.update(lastdate)
    return 'done'

app.add_url_rule("/search/", "search", search, methods=["POST"])
app.add_url_rule("/populate/", "populate", insert, methods=["POST"])
app.add_url_rule(
    "/search_trans/", "search_trans", search_trans, methods=["POST"]
)
app.add_url_rule(
    "/populate_trans/", "populate_trans", insert_trans, methods=["POST"]
)
app.add_url_rule(
    "/find_image/", "find_image", find_image, methods=["POST"]
)
app.add_url_rule(
    "/get_latest/", "search_latest", search_latest, methods=["GET"]
)
app.add_url_rule(
    "/update_cluster/", "update_cluster", update_cluster, methods=["GET"]
)
logging.debug("Api has been initialized")



if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(host="127.0.0.1", debug=False, threaded=False)


