import requests
import ast

search_url = 'http://127.0.0.1:5000/search/'
pop_url = 'http://127.0.0.1:5000/populate_trans/'
res = requests.post(pop_url, json={})

result_list = []
rec_dict = {}
i = 0


def get_old_db():
    """
    make request to database
    :return: data
    """
    req = requests.post(search_url, json={})
    data = ast.literal_eval(req.text)
    data_new = data[0]['response']['items']
    return data_new


def transform_data(data):
    """
    :param data: get mongodb dict
    :return: structured dict with {rec['id']:{ 'ownerid': rec['owner_id'], 'photos': list_photo}}
    """
    i = 0
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


def populate_data(data):
    for req in data:
        print(data[req])
        res = requests.post(pop_url, json=data[req])
    return res


if __name__ == "__main__":
    data = get_old_db()
    data_new = (transform_data(data))
    populate_data(data_new)

# how-to build db schema
# vk_wall_identificator = 'https://vk.com/wall'+'owner_id' + '_' + 'id'
