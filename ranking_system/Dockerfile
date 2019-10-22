FROM python:3.7.2
# pkg for ranking-system
RUN pip3 install opencv-python==3.4.2.17 opencv-contrib-python==3.4.2.17 pillow ipython
RUN apt-get update && apt-get install -y ipython
# pkg for mongo, api-gateway
RUN pip3 install pymongo flask Flask Flask-API requests dramatiq
# search for rf
RUN pip3 install keras sklearn tf-estimator-nightly==1.12.0.dev20181208 tf-nightly==1.14.1.dev20190409
COPY codebase/ /codebase
WORKDIR /codebase
CMD ["python3 api_server.py"]
