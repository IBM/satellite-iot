import json
import requests
from flask_cors import CORS
import pandas as pd
import os
from flask import Flask, jsonify, json, request, render_template

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)


@app.route('/')
def my_form():
    return render_template('link.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['url']
    return render_template('data.html', data=text)


port = os.getenv('VCAP_APP_PORT', '8080')
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)