#!/usr/bin/env python3

from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

private_key = input('Enter private key: ')
message = input('Enter message: ')

try:
    message = open(message, 'rb').read()
except:
    pass

pkey = RSA.import_key(open(private_key).read())
h = SHA256.new(message)
signature =  pss.new(pkey).sign(h)

f = open('signature.txt', 'wb')
f.write(signature)
f.close()


