""" Password generator program """

import random
from string import ascii_letters, digits

PASSWORD_SIZE = 16

chars = ascii_letters + digits + '!#$%&*/'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(PASSWORD_SIZE)))
