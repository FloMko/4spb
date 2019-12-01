# functional module
import codebase.dbHelper as dbHelper

# get config
import yaml

cfg = yaml.safe_load(open("../codebase/config.yaml"))

url = cfg["test"]["mongodb"]
database = cfg["database"]
collection = cfg["collection"]
collection_new = cfg["collection_new"]

new_db = dbHelper.Db(url, database, collection_new)
old_db = dbHelper.Db(url, database, collection)


def test_new_database_init():
    """check connection to new db"""
    isinstance(new_db.search_record({}), dict)

def test_old_database_init():
    """check connection to old db"""
    isinstance(old_db.search_record({}), dict)
