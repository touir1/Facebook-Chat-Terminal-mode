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

class Buffer:
    def __init__(self, buffer = ""):
        self.buffer = buffer

    def getBuffer(self):
        return self.buffer

    def addChar(self,char):
        if char == '\b':
            self.buffer = self.buffer[:-1]
        else:
            self.buffer += char

    def addToBuffer(self,toAdd):
        self.buffer += toAdd

    def clearBuffer(self):
        self.buffer = ""

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