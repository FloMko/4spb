# functional module
import codebase.db_helper as db_helper
# get config
import yaml

cfg = yaml.safe_load(open("../codebase/config.yaml"))

mongourl = cfg['test']['mongourl']
database = cfg['database']
collection = cfg['collection']
collection_new = cfg['collection_new']

new_db = db_helper.Db(mongourl, database, collection_new)
old_db = db_helper.Db(mongourl, database, collection)

def test_new_database_init():
    """check connection to new db"""
    isinstance(
        new_db.search_records({}),
        dict)

def test_old_database_init():
    """check connection to old db"""
    isinstance(
        old_db.search_records({}),
        dict)