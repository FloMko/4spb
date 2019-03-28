import requests
import ast

pop_url = 'http://127.0.0.1:5000/populate/'
res = requests.post(pop_url,json={})

search_url = 'http://127.0.0.1:5000/search/'
req = requests.post(search_url,json={})
data = ast.literal_eval(req.text)
print(data[0]['response']['items'][0])

# how-to build db schema
vk_wall_identificator = 'https://vk.com/wall'+'owner_id' + '_' + 'id'