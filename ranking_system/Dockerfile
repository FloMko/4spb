FROM python:3.7.2
# pkg for ranking-system
RUN pip3 install opencv-python==3.4.2.17 opencv-contrib-python==3.4.2.17 sklearn pandas
# pkg for mongo, api-gateway
RUN pip3 install pymongo flask Flask Flask-API
COPY codebase/ /codebase