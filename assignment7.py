#!/usr/bin/env python3

from threading import Thread
from queue import Queue
from flask import Flask, request, jsonify, session
from hashlib import sha256

app = Flask(__name__)

#app.secret_key = b'6d\xbeY\xf8\x1d\x95\xe1\xec\xa5_\xcf\x9c2\xdb\x03\xeem\x80\x1c\xea\x03\xee\xa3'

@app.route('/start', methods = ['POST'])
def miner():
    data = request.get_json()
    mystr = data["data"]
    #print(mystr)

    def mine(mystr, queue):
        target = int.from_bytes(bytes.fromhex('0'*7 +'f'+'0'*56), 'big')
        max_iter = 100000000000000

        for x in range(max_iter):
            #print('Trying', x)
            hash_str = mystr + str(x)
            hash256 = sha256(hash_str.encode()).digest()

            if int.from_bytes(hash256, 'big') < target:
                queue.put(x)
                break
    global queue
    queue = Queue()
    t = Thread(target = mine, args = [mystr, queue])
    t.start()

    return 'Started mining!', 200

@app.route('/result')
def Status():
    try:
        nonce = queue.get_nowait()
        return jsonify({"result":"found","nonce":nonce})
    except:
        return jsonify({"result":"searching","nonce":-1})

if __name__ == '__main__':
    app.run(host = '', port = 2019, debug = True)






