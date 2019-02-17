docker build  -t ranking-system .
docker run -ti --rm -v /home/flomko/Project/priv/4spb/4spb/ranking_system/dataset:/dataset ranking-system bash