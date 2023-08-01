""" File hider """

import ctypes

hide_attribute = 0x02

returns = ctypes.windll.kernel32.SetFileAttributesW('hide.txt', hide_attribute)

if returns:
    print('File has been hidden.')
else:
    print('File has not been hidden.')
