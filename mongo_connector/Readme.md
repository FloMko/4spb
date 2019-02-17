docker build  -t pymongo .
docker run -d -p 5000:5000 -v /home/flomko/Project/priv/4spb/4spb/mongo_connector/codebase/:/codebase --name flask pymongo sh -c "python /codebase/api_server.py "