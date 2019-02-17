import ast
import requests
import shutil


# get all list of images
search_req = {}

res = requests.post('http://26ddd8cf.ngrok.io/search/', json=search_req)

list_val = ast.literal_eval(res.text)

list_photo = []

for obj in list_val[0]['items']:
    if 'attachments' in obj.keys():
        attachments_list = obj['attachments']
        for attach in attachments_list:
            if attach['type'] == 'photo':
                print(attach['photo']['photo_604'])
                list_photo.append(attach['photo']['photo_604'])


# domnload images
for photo_url in list_photo:
    response = requests.get(photo_url, stream=True)
    with open('../dataset/'+photo_url.split('/')[-1], 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response