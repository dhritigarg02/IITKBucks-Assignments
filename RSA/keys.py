#!/usr/bin/env python3

from Crypto.PublicKey import RSA

key_pair = RSA.generate(2048)

private_key = key_pair.exportKey("PEM")
public_key = key_pair.publickey().exportKey("PEM")

sk = open("privatekey.pem", "wb")
sk.write(private_key)
sk.close()

pk = open("publickey.pem", "wb")
pk.write(public_key)
pk.close()
