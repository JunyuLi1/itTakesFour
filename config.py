from chat import ds_messenger

class User():
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        self.contactobj = ds_messenger.DirectMessenger(ip,username, password)

    def load_chat_history(self):
        #check and load history
        #TODO: possible feature
        self.contactobj.store_chat_history()
