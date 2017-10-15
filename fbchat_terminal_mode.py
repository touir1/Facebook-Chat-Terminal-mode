from fbchat import Client
from fbchat.models import *
from optparse import OptionParser
import os
import getpass
import pickle as pkl
import hashlib
import sys
import principalScreen
from queue import Queue
from threading import Thread
from utils import *

_SESSION_FILE = "sessions.pkl"

parser = OptionParser(usage='Usage: %prog [options]')
parser.add_option("-u", "--username", dest="username",
                  help="the username for the facebook account", metavar="USER")
parser.add_option("-p", "--password", dest="password",
                  help="the password for the facebook account", metavar="PASSWORD")

class User:
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

class Session:
    def __init__(self, username, password, session):
        toEncode = username.lower()+':'+password
        self.authdata = hashlib.sha512(toEncode.encode()).hexdigest()
        self.session = session

class CustomClient(Client):
    def startThread(self,thread_id):
        self.ThreadNow = thread_id
        self.ThreadStarted = True
        self.queue = Queue(maxsize=0)

    def getThreadName(self):
        return self.fetchThreadInfo(self.ThreadNow).name

    def stopThread(self):
        self.ThreadStarted = False

    def getMessage(self):
        return self.queue.get()

    def isThereMessage(self):
        return not self.queue.empty()

    def isStopThread(self):
        return not self.ThreadStarted
    
    def onMessage(self, mid, author_id, message, thread_id, thread_type, ts, metadata, msg, **kwargs):
        if self.ThreadStarted and self.ThreadNow == author_id:
            self.queue.put(message)
            #print(author_id,' : ',msg)
        pass

def script():
    (options, args) = parser.parse_args()

    username = None
    password = None
    client = None
    sessions = []
    session = None
    authdata = None
    connectedUID = None
    connected = None
    connectedName = None

    try:
        with open(_SESSION_FILE, 'rb') as inp:
            sessions = pkl.load(inp)
    except Exception as ex:
        print('no session detected')

    if options.username is not None:
        username = options.username
    if options.password is not None:
        password = options.password

    if username is None and password is not None:
        print('error: you need to set the username and the password')
        quit()
    if username is not None and password is None:
        password = getpass.getpass('Password: ')
    if username is None and password is None:
        print('Username: ', end='', flush=True)
        username = input()
        password = getpass.getpass('Password: ')

    try:
        toEncode = username.lower()+':'+password
        authdata = hashlib.sha512(toEncode.encode()).hexdigest()
        index = -1
        for idx,s in enumerate(sessions):
            if s.authdata == authdata:
                session = s.session
                index = idx
                break
        client = CustomClient(username,password,session_cookies=session)
        session = client.getSession()
        if index!=-1:
            sessions[index].session = session
        else:
            sessions.append(Session(username,password,session))
            
        connectedUID = client.uid
        connected = client.fetchUserInfo(connectedUID)[connectedUID]
        connectedName = connected.name
        with open(_SESSION_FILE, 'wb') as f:
            pkl.dump(sessions, f)
    except Exception as ex:
        print(ex)
        print('Login failed, Check email/password.')
        quit()

    users = {}
    for u in client.fetchAllUsers():
        users[u.uid] = u.name
    users[connectedUID] = connectedName

    principalScreen.openScreen(client, session)
    
    #randomThread = client.searchForThreads('random')[0]
    #client.sendMessage('random msg from python',thread_id=randomThread.uid, thread_type=randomThread.type)

##    print('last messages:')
##    threads = client.fetchThreadList(offset=0, limit=10)
##    for thread in threads:
##        messages = client.fetchThreadMessages(thread_id= thread.uid, limit=20)
##        print('------------------------------------------')
##        print(thread.name)
##        print('########################')
##        for msg in reversed(messages):
##            m = None
##            if msg.text is not None:
##                m = msg.text.translate(non_bmp_map)
##            print(users[msg.author],':',m)
##        print('------------------------------------------')

if __name__ == "__main__":
    script()
    
