from fbchat import Client
from fbchat.models import *
from optparse import OptionParser
import os
import getpass
import pickle as pkl

_SESSION_FILE = "session.pkl"

def console_clear():
    os.system('clear')

parser = OptionParser(usage='Usage: %prog [options]')
parser.add_option("-c", "--username", dest="username",
                  help="the username for the facebook account", metavar="USER")
parser.add_option("-v", "--password", dest="password",
                  help="the password for the facebook account", metavar="PASSWORD")

class User:
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

def script():
    (options, args) = parser.parse_args()

    username = None
    password = None
    client = None
    session = None
    connectedUID = None
    connected = None
    connectedName = None

    try:
        with open(_SESSION_FILE, 'rb') as inp:
            session = pkl.load(inp)
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
        password = getpass.getpass('Password:')
    if username is None and password is None:
        print('Username: ', end='', flush=True)
        username = input()
        password = getpass.getpass('Password: ')

    try:
        client = Client(username,password,session_cookies=session)
        session = client.getSession()
        connectedUID = client.uid
        connected = client.fetchUserInfo(connectedUID)[connectedUID]
        connectedName = connected.name
        with open(_SESSION_FILE, 'wb') as f:
            pkl.dump(session, f)
    except Exception as ex:
        print(ex)
        print('Login failed, Check email/password.')
        quit()

    users = {}
    for u in client.fetchAllUsers():
        users[u.uid] = u.name
    users[connectedUID] = connectedName
    threads = client.fetchThreadList(offset=0, limit=10)
    randomThread = client.searchForThreads('random')[0]
    client.sendMessage('random msg from python',thread_id=randomThread.uid, thread_type=randomThread.type)
    print('last messages:')
    for thread in threads:
        messages = client.fetchThreadMessages(thread_id= thread.uid, limit=20)
        print('------------------------------------------')
        print(thread.name)
        print('########################')
        for msg in reversed(messages):
            print(users[msg.author],':',msg.text)
        print('------------------------------------------')
    

if __name__ == "__main__":
    script()
    
