#!/usr/bin/python
import os
import sys
import binascii
import time

           ################ Description ##################
# This is the Bread and butter of the Iron Encryption Method(IEM), This is
# where all of the Encryption and Decryption happens.

# Takes string data and transforms it into Hex Data.
def encode(target_data):
    encode_list = []
    for en_step in list(target_data):
        target_data = en_step.encode("hex")
        encode_list.append(target_data)
    target_data = ':'.join(encode_list)
    return target_data

# Takes Hex data and turns it into a string. 
def decode(target_data):
    decode_list = []
    for de_step in target_data.split(':'): 
        target_data = de_step.strip().decode("hex")
        decode_list.append(target_data)
    target_data = ''.join(decode_list)
    return target_data

# Caller for the IEM System.
def iron_caller(args, key_data, target_data):
    formatted_data = []
    if args.encrypt and not args.decrypt:
        raw_bin = encode(target_data)
    if args.decrypt and not args.encrypt:
        raw_bin = target_data
    bin_list = raw_bin.split(':')
    if len(key_data) < 64:
        block_size = len(key_data)
    else:
        block_size = 64
    block_list = [bin_list[x:x+block_size] for x in range(0, len(bin_list),block_size)]
    for block_step in block_list:
        for index, bit_step in enumerate(block_step):
            try:
                output = str(hex(int(bit_step, 16) ^ int(list(key_data)[index],16))).replace('0x', '')
                # This is a Fix for New Lines within a File..
                if output == 'a':
                    output = '0a'
            except Exception as e:
                output = bit_step
            formatted_data.append(output)
    formatted_data = ':'.join(map(str, formatted_data))
    return formatted_data
