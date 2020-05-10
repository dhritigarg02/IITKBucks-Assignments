#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256

pub_key_path = input("Please enter your public key: ")
uncryp_txt = input("Please enter unencrypted message: ")
signature_file = input("Please enter signature: ")

try:
    message = open(uncryp_txt).read()
except:
    message = uncryp_txt

signature = open(signature_file, 'rb').read()

pub_key = RSA.import_key(open(pub_key_path).read())
h = SHA256.new(message.encode())
verifier = pss.new(pub_key)

try:
    verifier.verify(h, signature)
    print('Signature verified!')
except:
    print('Verification failed!')







