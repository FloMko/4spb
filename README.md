# 4spb
application for search for lost pets
database based on https://vk.com/yapoteryalsyaspb
##Reference
###
This app is interface (with bot/web version in future) with ai-driven core  
Feel free to ask me about how it run and why it's worked
### goals
improve ability to find any lost pet with large human collaboration
## History of collobarations
2019 02/14-15 https://gitlab.com/bkovesh/findpet https://gitlab.com/bkovesh https://vk.com/teplitsast
### local build for project
docker-compose up -d --build
###code delivery
ansible-playbook site.yml -i staging -l gcp

### Prereqriement
shoudl place .env file in root folder like env.example

replicated by hand between https://github.com/FloMko/4spb https://gitlab.com/flomko/4spb