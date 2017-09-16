from fbchat import Client
from fbchat.models import *
from optparse import OptionParser
import os
import getpass

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

def getUserFromUID(users, uid):
    for user in users:
        if uid == user.uid:
            return user
    return User()

def script():
    (options, args) = parser.parse_args()

    username = None
    password = None
    client = None

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
        client = Client(username,password)
    except:
        print('Login failed, Check email/password.')
        quit()

    users = [User(u.uid, u.name) for u in client.fetchAllUsers()]
    threads = client.fetchThreadList()
    print('last messages:')
    for thread in threads:
        message = client.fetchThreadMessages(thread_id= thread.uid, limit=1)[0]
        print('------------------------------------------')
        print(thread.name)
        print('############')
        print(message.text)
        #print(message.__dict__)
        print('------------------------------------------')
        
    #print([a.text for a in messages])
    

if __name__ == "__main__":
    script()
    
