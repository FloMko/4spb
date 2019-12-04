FROM python:3.7.2
RUN apt-get update && apt-get install -y ipython=5.1.0-3 --no-install-recommends && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY codebase/ /codebase
WORKDIR /codebase
# pkg for ranking-system
RUN pip3 install -r requirements.txt
CMD ["python3 main.py"]
