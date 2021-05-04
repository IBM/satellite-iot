import json
import requests
from flask_cors import CORS
import pandas as pd
import os
from flask import Flask, jsonify, json, request
import datetime

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)


def simulation():
        now = datetime.datetime.now()
        x = now.strftime("%Y-%m-%d %H:%M:%S")
        df = pd.read_csv('IoT-file.csv')
        c1 = df.sample()
        c1.columns =['container1_temperature']
        c1 = c1.to_json(orient='records')[1:-1].replace('},{', '} {')
        c2 = df.sample()
        c2.columns =['container2_temperature']
        c2 = c2.to_json(orient='records')[1:-1].replace('},{', '} {')
        c3 = df.sample()
        c3.columns =['container3_temperature']
        c3 = c3.to_json(orient='records')[1:-1].replace('},{', '} {')
        c4 = df.sample()
        c4.columns =['container4_temperature']
        c4 = c4.to_json(orient='records')[1:-1].replace('},{', '} {')
        c5 = df.sample()
        c5.columns =['container5_temperature']
        c5 = c5.to_json(orient='records')[1:-1].replace('},{', '} {')

        frames = []
        frames.append(json.loads(c1))
        frames.append(json.loads(c2))
        frames.append(json.loads(c3))
        frames.append(json.loads(c4))
        frames.append(json.loads(c5))

        details = {}
        j = 0 
        for i in frames:
            if j == 0:
                j = j + 1
                details['container1_temperature'] = i['container1_temperature']
            elif j == 1:
                j = j + 1
                details['container2_temperature'] = i['container2_temperature']
            elif j == 2:
                j = j + 1
                details['container3_temperature'] = i['container3_temperature']
            elif j == 3:
                j = j + 1
                details['container4_temperature'] = i['container4_temperature']
            elif j == 4:
                j = j + 1
                details['container5_temperature'] = i['container5_temperature']

        details['date'] = x
        return jsonify(details)

@app.route("/")
def main():
    return simulation()

port = os.getenv('VCAP_APP_PORT', '8080')
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)