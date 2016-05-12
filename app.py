import json

from flask import Flask, render_template, send_file, jsonify,current_app
from os import listdir
from os.path import isfile, join
import requests



app = Flask('stalky')


@app.route('/home')
def index():
    return current_app.send_static_file("main.html")

@app.route('/data/<int:uid>')
def get_data_for_uid(uid):
    return send_file("generated_graphs/csv/{uid}.csv".format(uid=uid))


@app.route('/api/list')
def get_list():
    return json.dumps(json.load(open('names.json')))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
