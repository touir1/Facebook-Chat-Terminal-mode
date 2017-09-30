from utils import *

def script(client, session):
    choix = 0
    while choix<1 or choix>3:
        console_clear()
        print('choisir un numéro:')
        print('1- voir la liste des messages')
        print('2- envoyer un message')
        print('3- quitter l\'application')
        choix = to_int(input('\nchoix: '))

    if choix == 3:
        quit()
    
