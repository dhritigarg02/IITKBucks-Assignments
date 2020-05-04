#!/usr/bin/env python3

import hashlib

max_iter = 100000000
my_str = input('Enter your data : ')

for x in range(1,max_iter):

    hash_str = my_str + str(x)
    hash256 = hashlib.sha256(hash_str.encode())
    hex_hash = hash256.hexdigest()

    if hex_hash[0:4] == '0000' and hex_hash[4:64] != 'f'* 60 :
        print('Your data with the magic number is : ',hash_str)
        break
