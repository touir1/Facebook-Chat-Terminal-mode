import os

def to_int(var):
    try:
        result = int(var)
        return result
    except:
        return 0

def console_clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
