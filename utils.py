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
    sub = substring.lower().split()
    sub.sort()
    s = string.lower().split()
    s.sort()
    return ''.join(sub) == lcs(''.join(sub),''.join(s))


def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result


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