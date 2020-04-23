#!/usr/bin/env python3

import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hash', methods = ['POST'])

def hash():
   data = request.get_json()
   hash256 = hashlib.sha256(data["data"].encode())
   return jsonify({"hash":hash256.hexdigest()})


if __name__ == '__main__':
   app.run(host = '', port = 8787)
