import hashlib

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


class User:
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name


class Session:
    def __init__(self, username, password, session):
        toEncode = username.lower()+':'+password
        self.authdata = hashlib.sha512(toEncode.encode()).hexdigest()
        self.session = session

