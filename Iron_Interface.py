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

<To Generate a Key: use Iron_key_Generator.py>
<For more info try: python Iron_Interface.py --help>
----------------------------------------------------------
"""

def create_args():
    parser = argparse.ArgumentParser(description='This is a Script that takes Data and a symmetric key to Encrypt or Decrypt user data.', usage=USAGE)
    parser.add_argument('-k', '--sym_key', help='- Path to the Symmetric Key.[String]', type=str, required=True)
    parser.add_argument('-f', '--file', help='- Path to an input file.[String]', default=False)
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

    key_data = IE.pull_key_data(args.sym_key)

    # reads the File given...
    if args.file:
        if not os.path.isfile(args.file):
            print 'Error: %s does not seem to be a file! -- Printing Help' % args.file
            parser.print_help()
            sys.exit()
        fr = open(args.file, 'r')
        target_data = fr.read(); fr.close()
    else:
        print 'Error need a File...'
        sys.exit()

    final = IE.iron_caller(args.encrypt, args.decrypt, key_data, target_data)

    fw = open(args.file, 'w')
    fw.write(final); fw.close()

if __name__ == "__main__":
    sys.exit(main())
