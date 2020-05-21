#!/usr/bin/env python3

from tx import *
import hashlib

num_inputs = int(input('Enter number of inputs: '))
inputs = []

print('\n')

for i in range(num_inputs):

    transID = input('Enter transaction ID for input {}: '.format(i+1))
    index = input('Enter index for input {}: '.format(i+1))
    signature = input('Enter signature for input {}: '.format(i+1))
    print('\n')

    inputs.append(Input(transID, index, signature))

num_outputs = int(input('Enter number of outputs: '))
outputs = []
print('\n')

for i in range(num_outputs):

    amount = input('Enter amount for output {}: '.format(i+1))
    publickey = input('Enter path to the public key for output {}: '.format(i+1))
    print('\n')

    outputs.append(Output(amount, publickey))

transaction = Tx(num_inputs, inputs, num_outputs, outputs)

tx_hash = hashlib.sha256(transaction._bytes_).hexdigest()

fh = open(tx_hash + '.dat', 'wb')
fh.write(transaction._bytes_)
fh.close()






