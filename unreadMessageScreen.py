from utils import *
import principalScreen
import sendMessageScreen


def openScreen(client, session):

    users = {}
    offset = 0
    jump = 10

    for u in client.fetchAllUsers():
        users[u.uid] = u.name
    users[client.uid] = client.fetchUserInfo(client.uid)[client.uid].name

    #repare
    #go back to menu
    #principalScreen.openScreen(client,session)
    #end get back to menu

    while True:
        console_clear()
        print('list of unread messages:')
        #buffer = Buffer()
        threads = []
        now = 0
        got = 10
        while(now<jump and got == jump):
            result = client.fetchThreadList(offset=offset, limit=jump)
            got = len(result)
            for idx, thread in enumerate(result):
                is_read = client.fetchThreadMessages(thread_id=thread.uid, limit=1)[0].is_read
                if not is_read:
                    threads.append(thread)
                    now += 1
                if now == jump:
                    break
            #print('now:',now,' offset:',offset)
            if now<jump and got == jump:
                offset += jump
        threads = client.fetchUnread()
        for idx, thread in enumerate(threads):
            messages = client.fetchThreadMessages(thread_id= thread.uid, limit=1)
            #buffer.push('------------------------------------------\n')
            print('------------------------------------------')
            #buffer.push(idx+1,'-',thread.name,'(last: ',users[messages[0].author],'): ',toUTF8(messages[0].text)+'\n')
            print(idx+1,'-',thread.name,'(last: ',users[messages[0].author],'): ',toUTF8(messages[0].text))

        print('------------------------------------------')

        options = ['b','e']

        if offset !=0:
            print('p - previous')
            options.append('p')
        if len(threads) == jump:
            print('n - next')
            options.append('n')
        print('b - back to main menu')
        print('e - exit')

        choice = input('choice: ')

        if choice in options:
            if choice == 'e':
                break
            elif choice == 'b':
                principalScreen.openScreen(client, session)
            elif choice =='n':
                offset += jump
            else:
                offset -= jump
        elif isInt(choice) and (1 <= to_int(choice) <= jump):
            sendMessageScreen.openScreen(client,session,threads[to_int(choice)-1])
            break

