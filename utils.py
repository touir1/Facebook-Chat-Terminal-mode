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


def containByWords(substring,string):

    sub = substring.lower().split(' ')
    sub.sort()
    s = string.lower().split(' ')
    s.sort()
    return ' '.join(sub) in ' '.join(s)


def getchar():
    result = ''
    try:
        import msvcrt
        result = msvcrt.getch().decode('cp1252')
    except ImportError:
        import tty,termios
        def _unix_getch():
            """Get a single character from stdin, Unix version"""

            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())  # Raw read
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

            result = _unix_getch

    return result



def stopPrint():
    sys.stdout = open(os.devnull, "w")


def startPrint():
    sys.stdout = sys.__stdout__