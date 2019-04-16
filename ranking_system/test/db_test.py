# functional module
import codebase.db_helper as db_helper

mongourl = 'mongodb://root:rootPassXXX@127.0.0.1:27017/admin'
database = 'lostpets'
collection = 'dataset'
collection_new = 'datastore'
new_db = db_helper.Db(mongourl, database, collection_new)
old_db = db_helper.Db(mongourl, database, collection)

def test_new_database_init():
    """check connection to new db"""
    isinstance(
        new_db.search_record({}),
        dict)

def test_old_database_init():
    """check connection to old db"""
    isinstance(
        old_db.search_record({}),
        dict)