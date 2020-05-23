#!/usr/bin/env python3

import hashlib
import time

class block:

    def __init__(self, index, prev_hash, target, data):

        self.index = index
        self.prev_hash = bytes.fromhex(prev_hash)
        self.target = target
        self.data = open(data, 'rb').read()
        self.data_hash = hashlib.sha256(self.data).digest()

    def mine(self, max_nonce):

        block_header_inits = index.to_bytes(4, 'big') + self.prev_hash + self.data_hash + target.to_bytes(32, 'big')

        h = hashlib.sha256()
        h.update(block_header_inits)

        start_time = time.time()
        for nonce in range(max_nonce):

            h_copy = h.copy()
            timestamp = time.time_ns()
            h_copy.update(timestamp.to_bytes(8, 'big') + nonce.to_bytes(8, 'big'))

            if int.from_bytes(h_copy.digest(), 'big') < self.target :

                time_taken = time.time() - start_time
                self.header = block_header_inits + timestamp.to_bytes(8, 'big') + nonce.to_bytes(8, 'big')
                self.hash = h_copy.hexdigest()
                self.timestamp = timestamp
                self.nonce = nonce
                print('Time taken to find nonce: ',int(time_taken/60),'m',int(time_taken%60), 's')
                break

index = int(input('Enter index of block: '))
prev_hash = input('Enter hash of previous block: ')
target = int(input('Enter target: '), 16)
data = input('Enter path to block body file: ')

max_nonce = 100000000000

block1 = block(index, prev_hash, target, data)
block1.mine(max_nonce)

print('The found nonce value is: ', block1.nonce)
print('The timestamp for the block is: ', block1.timestamp)
print('The hash of the block is: ', block1.hash)










