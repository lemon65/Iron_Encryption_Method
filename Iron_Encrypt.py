#!/usr/bin/python
import os
import sys
import binascii
import time

           ################ Description ##################
# This is the Bread and butter of the Iron Encryption Method(IEM), This is
# where all of the Encryption and Decryption happens. 

def inv_shift_chars():
    # This will shift half the Chars to the back of the list
    print 'shift Chars'

def inv_shift_lists():
    # This will shift half the lists to the baack of the LIST
    print 'shift LISTS'

def shift_chars():
    # This will shift half the Chars to the back of the list
    print 'shift Chars'

def shift_lists():
    # This will shift half the lists to the baack of the LIST
    print 'shift LISTS'

def encode(string):
    string = bin(int(binascii.hexlify(string),16))
    return string

def decode(bin_data):
    out_put = int(bin_data, 2)
    string = binascii.unhexlify('%x' % out_put)
    return string

def iron_caller(args, key_data, target_data):
    formatted_data = []
    if args.encrypt and not args.decrypt:
        raw_bin = encode(target_data)
    if args.decrypt and not args.encrypt:
        raw_bin = target_data

    if len(key_data) < 128:
        block_size = len(list(key_data))
    else:
        block_size = 128
    bit_list = [raw_bin[i:i+block_size] for i in range(0, len(raw_bin), block_size)]
    for block_step in bit_list:
        for index, bit_step in enumerate(block_step):
            try:
                output = int(bit_step) ^ int(list(key_data)[index])
            except Exception:
                output = bit_step
            formatted_data.append(output)
    formatted_data = ''.join(map(str, formatted_data))
    return formatted_data
