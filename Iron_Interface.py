#!/usr/bin/python

import os
import sys
import binascii
import time
import argparse
import Iron_Encrypt as IE

################ Description ##################
# This is a Script that takes User data and a symmetric key, Then calls Iron_Encrypt

USAGE = """
----------------------------------------------------------

python Iron_Interface.py -e -k 'PATH_TO_KEY' -f 'PATH_TO_FILE'
<or>
python Iron_Interface.py -e -k 'PATH_TO_KEY' -s

<To Generate a Key: use Iron_key_Generator.py>
<For more info try: python Iron_Interface.py --help>
----------------------------------------------------------
"""

def create_args():
    parser = argparse.ArgumentParser(description='This is a Script that takes Data and a symmetric key to Encrypt or Decrypt user data.', usage=USAGE)
    parser.add_argument('-k', '--sym_key', help='- Path to the Symmetric Key.[String]', type=str, required=True)
    parser.add_argument('-f', '--file', help='- Path to an input file.[String]', default=False)
    parser.add_argument('-s', '--string', help='- Flag to use a string as an Input.[Flag]', action='store_true', default=False)
    parser.add_argument('-e', '--encrypt', help='- Flag to Encrypt data.[Flag]', action='store_true')
    parser.add_argument('-d', '--decrypt', help='- Flag to Decrypt data.[Flag]', action='store_true')
    args = parser.parse_args()
    return (args, parser)

def main():
    args, parser = create_args()
    if not os.path.isfile(args.sym_key):
        print 'Error: %s does not seem to be a file!' % args.sym_key
        sys.exit()
    if not (args.encrypt or args.decrypt):
        print 'Please Select a Mode (-e or -d), Also try --help for more info.'
        sys.exit()

    # Read the Key Data...
    kr = open(args.sym_key, 'r')
    key_data = kr.read();kr.close()
    key_data = key_data.split(':')

    # reads the File given...
    if args.file and not args.string:
        if not os.path.isfile(args.file):
            print 'Error: %s does not seem to be a file! -- Printing Help' % args.file
            parser.print_help()
            sys.exit()
        fr = open(args.file, 'r')
        target_data = fr.read(); fr.close()

    # Reads a raw input from the user
    if args.string and not args.file:
        target_data = raw_input("Please Enter Your Data: ")
        if not target_data:
            print "### Error you didn't Enter any Data! ### -- Printing Help"
            parser.print_help()
            sys.exit()

    crypt_count = 0
    while crypt_count < 2:
        final = IE.iron_caller(args, key_data, target_data)
        target_data = final
        if args.encrypt and not args.decrypt:
            pass
        if args.decrypt and not args.encrypt:
            target_data = IE.decode(target_data)
        crypt_count += 1

    if args.string:
        print '\nResult:%s' % target_data
    if args.file:
        fw = open(args.file, 'w')
        fw.write(target_data); fw.close()

if __name__ == "__main__":
    sys.exit(main())
