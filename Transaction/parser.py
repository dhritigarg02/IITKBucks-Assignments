#!/usr/bin/env python3 

from hashlib import sha256
from textwrap import TextWrapper

path = input('Enter path to transaction data file: ')

fh = open(path, 'rb')

print('Transaction ID: ', sha256(fh.read()).hexdigest(), '\n')
fh.seek(0)

num_inputs = int.from_bytes(fh.read(4), byteorder = 'big')
print('Number of inputs: {}\n'.format(num_inputs))

for i in range(num_inputs):

    print('\tInput ' + str(i+1) + ':')
    print('\t\tTransaction ID: ', fh.read(32).hex())
    print('\t\tIndex: ', int.from_bytes(fh.read(4), byteorder = 'big'))
    len_sig = int.from_bytes(fh.read(4), byteorder = 'big')
    print('\t\tLength of the signature: ', len_sig)
    print('\t\tSignature: ', fh.read(len_sig).hex(), '\n')

num_outputs = int.from_bytes(fh.read(4), byteorder = 'big')
print('Number of outputs: {}\n'.format(num_outputs))

for i in range(num_outputs):
    
    print('\tOutput ' + str(i+1) + ':')
    print('\t\tNumber of coins: ', int.from_bytes(fh.read(8), 'big'))
    len_pubkey = int.from_bytes(fh.read(4), 'big')
    print('\t\tLength of public key: ', len_pubkey)
    wrapper = TextWrapper(subsequent_indent = '\t\t            ')
    pubkey = wrapper.wrap(text = fh.read(len_pubkey).decode('utf-8'))
    print('\t\tPublic key: ', end = '')
    for line in pubkey: print(line)
    print('\n')

fh.close()






