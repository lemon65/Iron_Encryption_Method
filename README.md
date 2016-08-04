# Iron_Encryption_Method -- IEM
   * The Iron Encryption Method is an encryption program that is loosely based off of AES-Symmetric Encryption.
     I am looking to create something that will allow me to store sensitive data and be able to learn something in the
     process. Your free to use IEM if you would like, and I hope that it serves you well!

## Features:
   * Key-Based-Symmetric Encryption.
   * Takes Text Files and Strings.
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
    kr = open('Private_Key_20160803-150027', 'r')# Generate a key with "python Iron_Key_Generator.py"
    key_data = kr.read();kr.close()
    key_data = key_data.split(':')
    for i in data_list: 
        print 'Data: %s' % i # Print Normal data.
        final = IE.iron_caller(True, False, key_data, i)
        print '\tEncrypted data: %s' % final# Print encrypted data.
        final = IE.iron_caller(False, True, key_data, final)
        print '\t Decrpyted data: %s' % final# Print the decrypted data.

if __name__ == "__main__":
    sys.exit(main())
```

Output from Running the Above Code -- > 
```
  $ python test.py
  Data: Test Data Example...
          Encrypted data:
  1d:19:1b:56:5b:48:5d:50:4c:70:19:55:4c:52:72:14:42:45:53:64
           Decrpyted data: Test Data Example...
  Data: Number: 3343436565
          Encrypted data: 06:01:00:05:04:0c:03:05:07:06:19:0e:4a:56:54:59:43:78
           Decrpyted data: Number: 3343436565
  Data: Name: Bob Hope
          Encrypted data: 56:47:5a:7b:17:5a:5f:73:14:0f:5c:59:59:7d
           Decrpyted data: Name: Bob Hope
  Data: Test Data: FooBar
          Encrypted data: 41:56:77:5c:58:7e:10:0b:55:41:58:70:18:47:45:51:62
           Decrpyted data: Test Data: FooBar
```

## Installation:
   * Git Clone https://github.com/lemon65/Iron_Encryption_Method
   * python Iron_Key_Generator.py ---- OR ---- python Iron_Key_Generator.py -p "PASSWORD"
   * python Iron_Interface.py -k Private_Key_DATE -f file_name.txt -e
    * python Iron_Interface.py -k Private_Key_20160728-134234 -s -e
    * Enter a String that you want to encrypt. 
   * python Iron_Interface.py -k Private_Key_DATE -f file_name.txt -d
    * python Iron_Interface.py -k Private_Key_20160728-134234 -s -d
    * Enter a String that you want to decrypt. 

## Requirements:
   * Python 2.7.6

## Commands:
| Flags        | description |
| ------------- |:-------------:|
| --help| Command to list Help for the program. |
| -k | Path to the Symmetric Key.[String] |
| -f | Path to an input file.[String] |
| -s | Flag to use a string as an Input.[Flag] |
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
