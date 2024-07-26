import time
import json
from chat import ds_messenger
from database import *

class User():
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        self.contactobj = ds_messenger.DirectMessenger(ip,username, password)

    def store_all_chat_history(self):
        result = self.contactobj.retrieve_all()
        for item in result:
            store_chat_history('receive',self.username,item.recipient,item.timestamp,item.message)

    def store_new_chat_history(self):
        result = self.contactobj.retrieve_new()
        for item in result:
            store_chat_history('receive',self.username,item.recipient,item.timestamp,item.message)

    def store_send_history(self, contact, message):
        store_chat_history('send',self.username,contact,time.time(),message)

    def load_contact_history(self, contact):#群聊
        return get_chat_history(self.username, contact, 0)

    def get_all_contacts(self):
        return json.loads(get_contacts(self.username))


if __name__ == '__main__':
    user = User('168.235.86.101','VC1', 'VC')
    #messagestyle useless