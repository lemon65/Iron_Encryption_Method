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
