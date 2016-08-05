#!/usr/bin/python

import sys
import string
import random as rd
import Iron_Encrypt as IE
import argparse
import time

           ################ Notes ##################
# This is a Script that takes a password or not and generates a 
# symmetric key for the user to encrypt and decrypt data.

usage = """
----------------------------------------------------------
python Iron_key_Generator.py -p 'PASSWORD_HERE'

<or>

python Iron_key_Generator.py (to generate a password with a random int)
----------------------------------------------------------
"""
parser = argparse.ArgumentParser(description='This is a Script that takes a password or not and generates a symmetric key for the user to encrypt and decrypt data.', usage=usage)
parser.add_argument('-p', '--password', help='Password used when creating a Key.', type=str, default=False)
args = parser.parse_args()

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(rd.choice(chars) for _ in range(size))

def main():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file_name = 'Private_Key_%s' % timestr
    if args.password:
        bin_data = IE.encode(args.password)
    else:
        data_key = id_generator(128)
        bin_data = IE.encode(str(data_key))
    target = open(file_name, 'w')
    target.write(bin_data)
    target.close()
    print "New Private Key Created!: %s" % file_name

if __name__ == "__main__":
    sys.exit(main())
