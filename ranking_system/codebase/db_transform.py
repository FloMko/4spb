import requests
import ast


class Transform():
    """
    Class for transform db from front
    """

    def __init__(self):
        self.search_url = 'http://127.0.0.1:5000/search/'
        self.pop_url = 'http://127.0.0.1:5000/populate_trans/'

    def get_old_db(self):
        """
        make request to database
        :return: data
        """
        req = requests.post(self.search_url, json={})
        data = ast.literal_eval(req.text)
        data_new = data[0]['response']['items']
        return data_new


    def transform_data(self, data):
        """
        :param data: get mongodb dict
        :return: structured dict with {rec['id']:{ 'ownerid': rec['owner_id'], 'photos': list_photo}}
        """
        i = 0
        rec_dict = {}
        for rec in data:
            photos = []
            photos_name = []
            if 'attachments' in rec.keys():
                attachments_list = rec['attachments']
                for attach in attachments_list:
                    if attach['type'] == 'photo':
                        i = i + 1
                        photos.append(attach['photo']['photo_604'])
                        photos_name.append(attach['photo']['photo_604'].split('/')[-1])
                        rec_dict.update({i: {'postid': rec['id'], 'ownerid': rec['owner_id'], 'photos_url': photos,
                                             'photos_name': photos_name}})
        return rec_dict


    def populate_data(self, data):
        for req in data:
            res = requests.post(pop_url, json=data[req])
        return res

    def get_photos_urls(self, data):
        photos_list = []
        for record in data:
            for photo in data[record]['photos_url']:
                photos_list.append(photo)
        return photos_list


    def main(self):
        data = self.get_old_db()
        data_new = self.transform_data(data)
        return (self.get_photos_urls(data_new))
    # return data_new
        populate_data(data_new)

# how-to build db schema
# vk_wall_identificator = 'https://vk.com/wall'+'owner_id' + '_' + 'id'
