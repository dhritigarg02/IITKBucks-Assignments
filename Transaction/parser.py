#!/usr/bin/env python3 

from hashlib import sha256
from textwrap import TextWrapper

path = input('Enter path to transaction data file: ')

fh = open(path, 'rb').read()

print('Transaction ID: ', sha256(fh).hexdigest(), '\n')

num_inputs = int.from_bytes(fh[0:4], byteorder = 'big')
print('Number of inputs: {}\n'.format(num_inputs))

curr_index = 4

for i in range(num_inputs):

    print('\tInput ' + str(i+1) + ':')
    print('\t\tTransaction ID: ', fh[curr_index:curr_index + 32].hex())
    curr_index += 32
    print('\t\tIndex: ', int.from_bytes(fh[curr_index:curr_index + 4], byteorder = 'big'))
    curr_index += 4
    len_sig = int.from_bytes(fh[curr_index:curr_index + 4], byteorder = 'big')
    print('\t\tLength of the signature: ', len_sig)
    curr_index += 4
    print('\t\tSignature: ', fh[curr_index:curr_index + len_sig].hex(), '\n')
    curr_index += len_sig 

num_outputs = int.from_bytes(fh[curr_index:curr_index + 4], byteorder = 'big')
print('Number of outputs: {}\n'.format(num_outputs))

curr_index += 4

for i in range(num_outputs):
    
    print('\tOutput ' + str(i+1) + ':')
    print('\t\tNumber of coins: ', int.from_bytes(fh[curr_index:curr_index+8], 'big'))
    curr_index += 8
    len_pubkey = int.from_bytes(fh[curr_index:curr_index+4], 'big')
    print('\t\tLength of public key: ', len_pubkey)
    curr_index += 4
    wrapper = TextWrapper(subsequent_indent = '\t\t            ')
    pubkey = wrapper.wrap(text = fh[curr_index:curr_index + len_pubkey].decode('utf-8'))
    print('\t\tPublic key: ', end = '')
    for line in pubkey: print(line)
    print('\n')






