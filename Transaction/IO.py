#!/usr/bin/env python3

from tx import *
import hashlib

number_inputs = int(input('Enter number of inputs: '))
inputs = []

for i in range(number_inputs):

    transID = input('Enter transaction ID: ')
    index = input('Enter index : ')
    signature = input('Enter signature : ')

    inputs.append(Input(transID, index, signature))

number_outputs = int(input('Enter number of outputs: '))
outputs = []

for i in range(number_outputs):

    amount = input('Enter amount: ')
    publickey = input('Enter path to the public key: ')

    outputs.append(Output(amount, publickey))

transaction = Tx(number_inputs, inputs, number_outputs, outputs)

tx_hash = hashlib.sha256(transaction._bytes_).hexdigest()

fh = open(tx_hash + '.dat', 'wb')
fh.write(transaction._bytes_)
fh.close()






