""" Hash comparer """

import hashlib

file_a = 'file_a.txt'
file_b = 'file_b.txt'

hash1 = hashlib.new('sha256')

hash1.update(open(file_a, 'rb').read())

hash2 = hashlib.new('sha256')

hash2.update(open(file_b, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'\nFile: {file_a} is different from file: {file_b}.\n')
    print(f'Hash1: {hash1.hexdigest()}\nHash2: {hash2.hexdigest()}')
else:
    print(f'\nFile: {file_a} is the same as file: {file_b}.\n')
    print(f'Hash1: {hash1.hexdigest()}\nHash2: {hash2.hexdigest()}')
