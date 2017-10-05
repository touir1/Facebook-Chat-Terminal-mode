from utils import *

def openScreen(client, session):
    console_clear()
    print('list of messages:')
    
    users = {}
    for u in client.fetchAllUsers():
        users[u.uid] = u.name
    users[client.uid] = client.fetchUserInfo(client.uid)[client.uid].name

    threads = client.fetchThreadList(offset=0, limit=15)
    for idx, thread in enumerate(threads):
        messages = client.fetchThreadMessages(thread_id= thread.uid, limit=1)
        print('------------------------------------------')
        print(idx+1,'-',thread.name,'(last: ',users[messages[0].author],'): ',toUTF8(messages[0].text))
        
    
