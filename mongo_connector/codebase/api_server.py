# -*- coding: utf-8 -*-
from flask import request, url_for
#from flask_cors import CORS
from flask_api import FlaskAPI, status, exceptions
import json
import db_helper

app = FlaskAPI(__name__)


@app.route('/search/',methods=['POST'])
def search():
    profile = request.form.get("profile")
    image = request.form.get("image")
    return json.dumps(response)


@app.route('/populate/',methods=['POST'])
def insert():
    print("Posted data : {}".format(request.get_json()))
    # return "Hello World!"
    data = request.get_json()
    print(data)
    data_new = db_helper.read_request(data)
    res = db_helper.write_record(data_new)
    return res


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
