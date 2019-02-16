# -*- coding: utf-8 -*-
from flask import request, url_for
#from flask_cors import CORS
from flask_api import FlaskAPI, status, exceptions
import json


app = FlaskAPI(__name__)


@app.route('/search/',methods=['POST'])
def search():
    profile = request.form.get("profile")
    image = request.form.get("image")

    return json.dumps(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
