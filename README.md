[![Total alerts](https://img.shields.io/lgtm/alerts/g/FloMko/4spb.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/FloMko/4spb/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/FloMko/4spb.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/FloMko/4spb/context:python)
[![Language grade: JavaScript](https://img.shields.io/lgtm/grade/javascript/g/FloMko/4spb.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/FloMko/4spb/context:javascript)
# 4spb
application for search for lost pets
database based on https://vk.com/yapoteryalsyaspb
## Reference
This app is interface (with bot/web version in future) with ai-driven core  
### Description
Feel free to ask me about how it run and why it's worked
### goals
improve ability to find any lost pet with large human collaboration
### local build for project
docker-compose up -d --build
### collobarators
<https://gitlab.com/bkovesh>
###code delivery
ansible-playbook site.yml -i staging -l gcp --tags all,init
### Prereqriement
shoudl place .env file in root folder like env.example

replicated by hand between <https://github.com/FloMko/4spb> & <https://gitlab.com/flomko/4spb>