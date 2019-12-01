import vectorize as vectorize
import imageHelper as imageHelper
import cluster as cluster
import dbHelper as dbHelper
import logging
import numpy

# get config
import yaml


class Find:
    """
    helper for search image process
    """

    def __init__(self):
        cfg = yaml.safe_load(open("config.yaml"))
        mongourl = cfg["mongourl"]
        database = cfg["database"]
        collection = cfg["collection"]
        collection_new = cfg["collection_new"]
        self.sources = cfg["dataset_path"]
        self.temp_path = cfg["temp_path"]
        self.cluster = cluster.Cluster()
        self.vec = vectorize.Vectors()
        self.db = dbHelper.Db(mongourl, database, collection)
        self.db_new = dbHelper.Db(mongourl, database, collection_new)

    def prepare_image(self, photo):
        """
        download by url and resize image - prepare for transformation image2vec
        :param photo: url
        :return: abs posix path
        """
        helper = imageHelper.Helper(self.temp_path)
        path = helper.download_image(photo_url=photo)
        helper.resize(path)
        return path

    def vector_image(self, path, n_neighbor):
        vect = self.vec.get_vector(path)
        dist, indices = self.cluster.find_nearest(vect, n_neighbor)
        images = imageHelper.Helper(self.sources).get_images()
        near = self.cluster.get_similar_images(images, dist, indices)
        return near[:5]

    def get_records(self, record):
        """
         search in db against records
        :param record list of photo's to search
        :return: list of
        """
        logging.debug('get_records debug' + str(record))
        logging.debug(record[1])
        logging.debug(record[0])
        image = record[0].split('/')[-1]
        if not isinstance(record, numpy.float32):
            response = [
                self.db_new.search_record(
                    {"photos_name": {"$elemMatch": {"$in": [image]}}}
                ),
                float(record[1]),
                ]
            return response
        else:
            logging.debug('trying to find numpy type')

    @staticmethod
    def format_record(records):
        logging.debug(records)
        response = []
        for record in records:
            url = 'https://vk.com/wall' + str(record[0]['ownerid']) + '_' + str(record[0]['postid']) + ' score: ' \
                                                                                + str(record[1])
            response.append(url)
        return response

    def main(self, photo):
        records = list()
        self.cluster.load()
        path = self.prepare_image(photo)
        n_neighbor = len(
            imageHelper.Helper(self.sources).get_images()
        )
        near = self.vector_image(path, n_neighbor)
        imageHelper.Helper(self.temp_path).remove_image(path)
        for record in (near[:5]):
            records.append(self.get_records(record))
        logging.debug("For records: " + str(records))
        response = self.format_record(records)
        logging.debug(
            "For search req: " + photo + " have been find: " + " ".join(response)
        )
        return response

    # how-to build db schema
    # vk_wall_identificator = 'https://vk.com/wall'+'owner_id' + '_' + 'id'
