import os
import sys

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

def to_int(var):
    try:
        result = int(var)
        return result
    except:
        return 0

def isInt(var):
    try:
        result = int(var)
        return True
    except:
        return False

def console_clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def toUTF8(string):
    if string is not None:
        return string.translate(non_bmp_map)
    return None
