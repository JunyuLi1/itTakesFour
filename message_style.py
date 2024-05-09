class Message:
    def __init__(self, message, time):
        self.receiver = None
        self.message = message
        self.time = time
    
    def get_time(self):
        return self.time
    
    def get_message(self):
        return self.message
    
    def __eq__(self, other):
        if not isinstance(other, Message):
            return 
        return (self.message == other.message) and (self.time == other.time)
    
    