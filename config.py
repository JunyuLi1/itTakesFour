from chat import ds_messenger
from database import *

class User():
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        self.contactobj = ds_messenger.DirectMessenger(ip,username, password)

    def store_all_chat_history(self):
        #check and store history
        # contact parts = {'SuperHammerB': {'SuperHammerB':[],'user:[]'}}
        #TODO: Possible feature
        result = self.contactobj.retrieve_all()
        for item in result:
            store_chat_history('new_info',self.username,item.recipient,item.timestamp,item.message)

    def store_new_chat_history(self):
        result = self.contactobj.retrieve_new()
        for item in result:
            store_chat_history('new_info',self.username,item.recipient,item.timestamp,item.message)

    def store_send_history(self, contact, message): #修改
        #store_chat_history('new_info',self.username,item.recipient,item.timestamp,item.message)
        pass


# if __name__ == '__main__':
#     user = User('168.235.86.101','VC1', 'VC')
#     user.store_all_chat_history()