import dbHelper as dbHelper

# logging
import logging

# get config
import yaml


class Transform:
    """
        Class for transform db from front
        """
    def __init__(self):
        cfg = yaml.safe_load(open("config.yaml"))
        mongourl = cfg["mongourl"]
        database = cfg["database"]
        collection = cfg["collection"]
        collection_new = cfg["collection_new"]
        self.db = dbHelper.Db(mongourl, database, collection)
        self.db_new = dbHelper.Db(mongourl, database, collection_new)
        self.photos_urls = []

    def get_old_db(self):
        """
        make request to database
        :return: data
        """
        data = self.db.search_records({})
        # data_new = data[0]['response']['items']
        return data

    def get_old_db_with_time(self, time):
        """
        let's find all object above timestamp
        :param time: time in mongodb
        :return:
        """
        data = self.db.search_records({"date": {"$gt": time}})
        # data_new = data[0]['response']['items']
        return data

    @staticmethod
    def transform_data(data):
        """
        :param data: get mongodb dict
        :return: structured dict with {rec['id']:{ 'ownerid': rec['owner_id'], 'photos': list_photo}}
        """
        i = 0
        rec_dict = {}
        for rec in data:
            date = rec['date']
            photos = []
            photos_name = []
            if "attachments" in rec.keys():
                attachments_list = rec["attachments"]
                for attach in attachments_list:
                    if attach["type"] == "photo":
                        i = i + 1
                        photos.append(attach["photo"]["photo_604"])
                        photos_name.append(attach["photo"]["photo_604"].split("/")[-1])
                        rec_dict.update(
                            {
                                i: {
                                    "postid": rec["id"],
                                    "ownerid": rec["owner_id"],
                                    "photos_url": photos,
                                    "photos_name": photos_name,
                                    "date": date
                                }
                            }
                        )
        return rec_dict

    def populate_data(self, data):
        for req in data:
            self.db_new.write_record(data[req])

    def get_photos_urls(self, data):
        """
        extract urls from data
        :param data: prepared im-memore ob
        :return: list of all urls from obj
        """
        photos_urls = []
        for record in data:
            for photo in data[record]["photos_url"]:
                photos_urls.append(photo)
        self.photos_urls = photos_urls
        return self.photos_urls

    def update(self, time):
        data = self.get_old_db_with_time(time)
        data_new = self.transform_data(data)
        self.populate_data(data_new)
        logging.debug("database has been populated")
        return self.get_photos_urls(data_new)

    def main(self):
        data = self.get_old_db()
        data_new = self.transform_data(data)
        self.populate_data(data_new)
        logging.debug("database has been populated")
        return self.get_photos_urls(data_new)


# how-to build db schema
# vk_wall_identificator = 'https://vk.com/wall'+'owner_id' + '_' + 'id'
