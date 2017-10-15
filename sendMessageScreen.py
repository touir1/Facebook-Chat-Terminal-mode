from utils import *
import os
from threading import Thread
import time

def receive(client):
  threadName = client.getThreadName()
  while not client.isStopThread():
      while(client.isThereMessage()):
          print('['+threadName+']: '+client.getMessage())


def openScreen(client,session,thread):
    if thread is not None:
        messages = client.fetchThreadMessages(thread_id=thread.uid, limit=10)
        for msg in messages:
            print('['+client.fetchThreadInfo(msg.author)[msg.author].name+']: '+toUTF8(msg.text))
        client.startThread(thread.uid)
        toSendMessage = input('['+client.fetchThreadInfo(client.uid)[client.uid].name+']: ')

