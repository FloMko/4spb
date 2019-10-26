import vectorize as vectorize
import image_helper as imagehelper
import cluster as cluster
import db_helper
import logging

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
        self.dataset_path = cfg["dataset_path"]
        self.temp_path = cfg["temp_path"]
        self.cluster = cluster.Cluster()
        self.vec = vectorize.Vectors()
        self.db = db_helper.Db(mongourl, database, collection)
        self.db_new = db_helper.Db(mongourl, database, collection_new)

    def prepare_image(self, photo):
        imhelp = imagehelper.Helper(dataset_path=self.temp_path)
        path = imhelp.download_image(photo_url=photo)
        imhelp.resize(path)
        return path

    def vector_image(self, path, n_neighbor):
        vect = self.vec.get_vector(path)
        dist, indices = self.cluster.find_nearest(vect, n_neighbor)
        images = imagehelper.Helper(self.dataset_path).get_images()
        near = self.cluster.get_similar_images(images, dist, indices)
        return near

    def get_records(self, near):
        response = []
        for photo in near[:5]:
            response.append(
                [
                    self.db_new.search_record(
                        {"photos_name": {"$elemMatch": {"$in": [photo[0]]}}}
                    ),
                    str(photo[1]),
                ]
            )
        return response

    def format_record(self, records):
        response = []
        for record in records:
            url = f"https://vk.com/wall{record[0]['ownerid']}_{record[0]['postid']} score: {record[1]}"
            response.append(url)
        return response

    def main(self, photo):
        self.cluster.load()
        path = self.prepare_image(photo)
        n_neighbor = len(
            imagehelper.Helper(dataset_path=self.dataset_path).get_images()
        )
        near = self.vector_image(path, n_neighbor)
        imagehelper.Helper(dataset_path=self.temp_path).remove_image(path)
        records = self.get_records(near)
        logging.debug("For records: ", records)
        response = self.format_record(records)
        logging.debug(
            "For search req: " + photo + " have been find: " + " ".join(response)
        )
        return response

    # how-to build db schema
    # vk_wall_identificator = 'https://vk.com/wall'+'owner_id' + '_' + 'id'
