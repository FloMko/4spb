import requests
import ast

pop_url = 'http://127.0.0.1:5000/populate/'
res = requests.post(pop_url, json={})

result_list = []
rec_dict = {}


def get_old_db():
    """
    make request to database
    :return: data
    """
    search_url = 'http://127.0.0.1:5000/search/'
    req = requests.post(search_url, json={})
    data = ast.literal_eval(req.text)
    data = data[0]['response']['items']
    return data


def transform_data(data):
    """
    :param data: get mongodb dict
    :return: structured dict with {rec['id']:{ 'ownerid': rec['owner_id'], 'photos': list_photo}}
    """

    for rec in data:
        list_photo = []
        if 'attachments' in rec.keys():
            attachments_list = rec['attachments']
            for attach in attachments_list:
                if attach['type'] == 'photo':
                    list_photo.append(attach['photo']['photo_604'])
            rec_dict.update({rec['id']: {'ownerid': rec['owner_id'], 'photos': list_photo}})
    return rec_dict


if __name__ == "__main__":
    data = get_old_db()
    print(transform_data(data))

# how-to build db schema
# vk_wall_identificator = 'https://vk.com/wall'+'owner_id' + '_' + 'id'
