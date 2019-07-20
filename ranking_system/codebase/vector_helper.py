import pickle
import logging
# get config
import yaml
import db_helper


class Helper:
    """
    for  high-level manipulation&
    """
    def __init__(self):
        # self.vector_structure = vectorize.Vectors()
        cfg = yaml.safe_load(open("config.yaml"))
        mongourl = cfg['mongourl']
        database = cfg['database']
        collection = cfg['collection_vectors']
        self.db = db_helper.Db(mongourl, database, collection)
        logging.debug('vec helper has been initialized')
        self.vectors_count = self.db_total_photos_count()

    def get_images_from_db(self):
        """
        extract image names from vectors scructure
        :param predictions:
        :return:
        """
        return self.db.collection.distinct('name')

    def write_to_db(self, vector_structure_line):
        """
        write vector structure to bd
        :param vector_structure_line: line in vectorize get_prediction format
        :param db: object, access to db
        :return: structured dict with {rec['id']:{ 'name': name_of_photo, 'vector': cnn vectors}}
        """
        name = vector_structure_line[0][0].decode('utf-8')
        vector = vector_structure_line[0][1]
        return self.db.write_record({'name': name, 'vector': pickle.dumps(vector)})

    def search_in_db(self, name):
        """
        searсh in db for vector by name
        :param name:
        :return:
        """
        return self.db.search_formatted_record({'name': name})

    def update_in_db(self, vector_structure_line):
        """
        write vector structure to bd
        :param vector_structure_line: line in vectorize get_prediction format
        :param db: object, access to db
        :return: structured dict with {rec['id']:{ 'name': name_of_photo, 'vector': cnn vectors}}
        """
        name = vector_structure_line[0][0].decode('utf-8')
        vector = vector_structure_line[0][1]
        return self.db.collection.update_one({'name': name},
                                             {"$set": {"vector": pickle.dumps(vector)}}, upsert=True).raw_result

    def db_total_photos_count(self):
        """
        just get all count of documents
        :return: count
        """
        return self.db.collection.count_documents({})
