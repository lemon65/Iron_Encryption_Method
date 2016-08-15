# Iron_Encryption_Method -- IEM [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
   * The Iron Encryption Method is an encryption program that is loosely based off of AES-Symmetric Encryption.
     I am looking to create something that will allow me to store sensitive data and be able to learn something in the
     process. Your free to use IEM if you would like, and I hope that it serves you well!

## Features:
   * Key-Based-Symmetric Encryption.
   * Iron_Interface is able to Take Text Files and encode them. 
   * Easy to import and use.
   * Reverses each data block for better encryption.
   * Able to Encrypt and Decrypt 21752 Lines, in under 3-Seconds.

## Example Code/w Output:
```py
#!/usr/bin/python
#Quick Example of importing Iron_Encrypt

import sys
import os
import Iron_Encrypt as IE

data_list = ['Test Data Example...',
             'Number: 3343436565',
             'Name: Bob Hope',
             'Test Data: FooBar']

def main():
    # Read the Key Data...
    key_data = IE.pull_key_data('Private_Key_20160803-150027')# Generate a Key with Iron_key_Generator.py 
    for i in data_list: 
        print 'Data: %s' % i # Print Normal data.
        final = IE.iron_caller(True, False, key_data, i)
        print '\tEncrypted data: %s' % final# Print encrypted data.
        final = IE.iron_caller(False, True, key_data, final)
        print '\tDecrpyted data: %s' % final# Print the decrypted data.

if __name__ == "__main__":
    sys.exit(main())
```

Output from Running the Above Code -- > 
```
$ python test.py
Data: Test Data Example...
        Encrypted data: tmj] %91Ll %*b2A\
        Decrpyted data: Test Data Example...
Data: Number: 3343436565
        Encrypted data: ouqagdul{#.6/3|
        Decrpyted data: Number: 3343436565
Data: Name: Bob Hope
        Encrypted data: ?3+pl7;|),0
        Decrpyted data: Name: Bob Hope
Data: Test Data: FooBar
        Encrypted data: ("W#tjU2-q?''
        Decrpyted data: Test Data: FooBar
```

## Installation:
   * Git Clone https://github.com/lemon65/Iron_Encryption_Method
   * python Iron_Key_Generator.py ---- OR ---- python Iron_Key_Generator.py -p "PASSWORD"
   * python Iron_Interface.py -k Private_Key_DATE -f file_name.txt -e
   * python Iron_Interface.py -k Private_Key_DATE -f file_name.txt -d

## Requirements:
   * Python 2.7.6

## Commands:
| Flags        | description |
| ------------- |:-------------:|
| --help| Command to list Help for the program. |
| -k | Path to the Symmetric Key.[String] |
| -f | Path to an input file.[String] |
| -e | Flag to Encrypt data.[Flag] |
| -d | Flag to Decrypt data.[Flag] |

## ToDo:
  * Refine Block Reverse.
  * Use more data from the created Key. 

## Help:
  * If you need help you can email me @ lemon65.twitch@gmail.com, or talk with me on my Team Speak
    (IP = ts.ramcommunity.com) user name is lemon65. 

## Notes:
  * None

## Thank you to:
  * Lemon65 and my father -- > "know alot about a little and a little about a lot" -- David (2013)

## Copyright:

#################### Copyright (c) 2016 RamCommunity #################

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do so
