import vectorize as vectorize
import image_helper as imagehelper
import cluster as cluster
import db_helper
import logging



class Find():
    """
    helper for search image process
    """
    def __init__(self):
        mongourl = 'mongodb://root:rootPassXXX@127.0.0.1:27017/admin'
        database = 'lostpets'
        collection = 'dataset'
        collection_new = 'datastore'
        self.dataset_path = '../dataset/'
        self.cluster = cluster.Cluster()
        self.vec = vectorize.Vectors()
        self.db = db_helper.Db(mongourl, database, collection)
        self.db_new = db_helper.Db(mongourl, database, collection_new)

    def prepare_image(self, photo):
        imhelp = imagehelper.Helper(dataset_path='../tmpdata/')
        path = imhelp.download_image(photo_url=photo)
        imhelp.resize(path)
        logging.debug(path + ' have been download')
        return path

    def vector_image(self, path):
        vect = self.vec.get_vector(path)
        dist, indices = self.cluster.find_nearest(vect)
        images = imagehelper.Helper(self.dataset_path).get_images()
        near = self.cluster.get_similar_images(images, dist, indices)
        return near

    def get_records(self, near):
        response = []
        for photo in near[:5]:
            print(photo)
            response.append([self.db_new.search_record({'photos_name': {'$elemMatch': {'$in': [photo[0]]}}}), str(photo[1])])
        return response

    def format_record(self, records):
        response = []
        for record in records:
            response.append('https://vk.com/wall'+str(record[0]['ownerid'])+'_'+str(record[0]['postid']) + ' score='+
                            str(record[1]))
        return response


    def main(self, photo):
        self.cluster.load()
        path = self.prepare_image(photo)
        near = self.vector_image(path)
        imagehelper.Helper(dataset_path='../tmpdata/').remove_image(path)
        logging.debug(path+"removed")
        records = self.get_records(near)
        return self.format_record(records)

    # how-to build db schema
    # vk_wall_identificator = 'https://vk.com/wall'+'owner_id' + '_' + 'id'