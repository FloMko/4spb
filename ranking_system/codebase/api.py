import requests
pop_url = 'http://127.0.0.1:5000/populate/'
res = requests.post(pop_url,json={})

search_url = 'http://127.0.0.1:5000/search/'
req = requests.post(search_url,json={})