#!/usr/bin/env python3

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

my_map = {}
my_peers = ['http://127.0.0.1:2021/']

@app.route('/')
def basic():
    return 'Server is running...'

@app.route('/add', methods = ['POST'])
def __add__():
    data = request.get_json()

    key = int(data['key'])
    value = data['value']

    if key in my_map : 
        pass
    else:
        my_map[key] = value
        for peer in my_peers:
            requests.post(peer + 'add', json = data)
            print('\nsent {}:{} to {}\n'.format(data['key'], data['value'], peer))
        return 'Set {} : {} successfully!'.format(key, value)
    return 'Key already in map'

@app.route('/list', methods = ['GET'])
def __list__():
    return jsonify(my_map)

if __name__ == '__main__':
    app.run(host = '', port = 2020, debug = True)

