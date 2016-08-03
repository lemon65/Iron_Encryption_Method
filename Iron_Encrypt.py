#!/usr/bin/python
import os
import sys
import binascii
import time

           ################ Description ##################
# This is the Bread and butter of the Iron Encryption Method(IEM), This is
# where all of the Encryption and Decryption happens.

# Reverses a List.
def reverse_list(target_list):
    return target_list[::-1]

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
        try:
            target_data = de_step.strip().decode("hex")
        except Exception as e:
            decode_list.append(de_step)
            print 'Hit Error on: %s, Keeping Hex data.' % de_step
        decode_list.append(target_data)
    target_data = ''.join(decode_list)
    return target_data

# Caller for the IEM System.
def iron_caller(encrypt, decrypt, key_data, target_data):
    formatted_data = []
    if not encrypt and not decrypt:
        return None
    if encrypt and not decrypt:
        raw_bin = encode(target_data)
    if decrypt and not encrypt:
        raw_bin = target_data
        #This checks that the data should be decrypted.
        try:
            sample_data = raw_bin.split(':')[0]
            if int(sample_data, 16):
                pass
        except Exception as e:
            return target_data

    bin_list = raw_bin.split(':')
    if len(key_data) < 64:
        block_size = len(key_data)
    else:
        block_size = 64
    block_list = [bin_list[x:x+block_size] for x in range(0, len(bin_list),block_size)]
    for block_step in block_list:
        if encrypt:
            block_step = reverse_list(block_step)
        block_buffer = []
        for index, bit_step in enumerate(block_step):
            try:
                output = str(hex(int(bit_step, 16) ^ int(key_data[index],16))).replace('0x', '')
                # This is a Fix for when the Hex Convert removes leading Zeros. 
                if len(output) == 1:
                    output = '0' + output
            except Exception as e:
                output = bit_step
            block_buffer.append(output)
        if decrypt:
            block_buffer = reverse_list(block_buffer)
        for data_step in block_buffer:
            formatted_data.append(data_step)
    formatted_data = ':'.join(map(str, formatted_data))
    if encrypt and not decrypt:
        pass
    if decrypt and not encrypt:
        formatted_data = decode(formatted_data)
    return formatted_data
