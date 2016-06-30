#!/usr/bin/python
import os
import sys
import binascii
import time

           ################ Description ##################
# This is the Bread and butter of the Iron Encryption Method(IEM), This is
# where all of the Encryption and Decryption happens.



# This will shift half the Chars to the back of the LIST
def shift_chars(args, block_size):
    print 'shift Chars'

# This will shift half the lists to the back of the LIST
def shift_lists(bit_list):
    half_lists = bit_list[:len(bit_list)/2]
    for half_step in half_lists:
        del bit_list[0]
        bit_list.append(half_step)
    return bit_list

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
    if len(key_data) < 10:
        block_size = len(key_data)
    else:
        block_size = 10
    bit_list = [bin_list[x:x+block_size] for x in range(0, len(bin_list),block_size)]
    
    # TODO -- Working on the Bit_List Shift...
    #bit_list = shift_lists(bit_list)

    print '----------------------------------------------------------'
    print 'Before: %s' % raw_bin
    print '----------------------------------------------------------'
    for block_step in bit_list:
        for index, bit_step in enumerate(block_step):
            try:
                output = str(hex(int(bit_step, 16) ^ int(list(key_data)[index],16))).replace('0x', '')
                # This is a Fix for New Lines within a File..
                if output == 'a':
                    output = '0a'
            except Exception as e:
                print e
                output = bit_step
            formatted_data.append(output)
    formatted_data = ':'.join(map(str, formatted_data))
    print '----------------------------------------------------------'
    print 'After: %s' % formatted_data
    print '----------------------------------------------------------'
    return formatted_data
