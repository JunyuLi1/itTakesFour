from chat import ds_messenger

class User():
    def __init__(self, ip, ucername, password):
        self.contactobj = ds_messenger.DirectMessenger(ip,ucername, password)
