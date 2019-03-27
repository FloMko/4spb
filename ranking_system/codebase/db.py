import db_helper as db_helper

mongourl = 'mongodb://root:rootPassXXX@127.0.0.1:27017/admin'
database = 'lostpets'
collection = 'dataset'


# import importlib
# importlib.reload(db_helper)
import db_helper as db_helper

db = db_helper.db(mongourl,database,collection)
# res = db.write_record({'1':'2'})
# print(res)
req = db.search_records({})
print(req)