""" Wordlist generator """

from itertools import permutations

word = input('Word to permute: ')

result = permutations(word, len(word))

for char in result:
    print(''.join(char))
