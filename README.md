# 4spb
search for lost pets 
## build 
### local build for project
docker-compose up -d --build
###code delivery
ansible-playbook site.yml -i staging -l gcp

### Prereqriement
shoudl place .env file in root folder like env.example

moved to https://gitlab.com/flomko/4spb
