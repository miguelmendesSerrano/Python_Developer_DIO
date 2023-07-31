""" Hash generator """

import hashlib

text = input('Text to encrypt: ')

menu = int(input('''
==== MENU ====
[1] MD5
[2] SHA1
[3] SHA256
[4] SHA512
==============
Choose one of the options (1, 2, 3 or 4): '''))

if menu == 1:
    result = hashlib.md5(text.encode('utf-8'))
    print(f'Hash MD5: {result.hexdigest()}')
elif menu == 2:
    result = hashlib.sha1(text.encode('utf-8'))
    print(f'Hash SHA1: {result.hexdigest()}')
elif menu == 3:
    result = hashlib.sha256(text.encode('utf-8'))
    print(f'Hash SHA256: {result.hexdigest()}')
elif menu == 4:
    result = hashlib.sha512(text.encode('utf-8'))
    print(f'Hash SHA512: {result.hexdigest()}')
else:
    print('Option invalid.')
