import vectorize as vectorize
import db_helper

import numpy as np
import pickle
import logging
# get config
import yaml


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
        self.vectors_count = get_total_photos_count()

    def get_images(self, predictions):
        """
        extract image names from vectors scructure
        :param predictions:
        :return:
        """
        return None

    def write_to_db(self,vector_structure_line):
        """
        write vector structure to bd
        :param vector_structure_line: line in vectorize get_prediction format
        :param db: object, access to db
        :return: structured dict with {rec['id']:{ 'ownerid': rec['owner_id'], 'photo_url': list_photo}}
        """
        name = vector_structure_line[0][0].decode('utf-8')
        vector = vector_structure_line[0][1]
        return self.db.write_record({'name': name, 'vector': pickle.dumps(vector)})

    def search_in_db(self, name):
        return self.db.search_formatted_record({'name': name})

    def get_total_photos_count(self, ):
        return self.db.search_formatted_record({}.count())
