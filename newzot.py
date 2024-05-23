import streamlit as st
import ds_messenger
from message_style import Message
import time

class Chat:
    def __init__(self, ip, account, password):
        self.contactobj = ds_messenger.DirectMessenger(ip, account, password)
        st.session_state.chat_logs = {
            "Alan": [Message("How's your pj2?", 1), Message("sounds good", 2), Message("bye", 3)],
            "SuperHammerA": [Message("Hello World", 1), Message("Nice to meet you", 2)],
            "SuperHammerD": [Message("Test1", 1), Message("Test2", 2)]
        }
        st.session_state.group_chat = {}
        self.friend = None
        self.result = None
        self.new = None

    def main(self):
        self.create_friendlist()
        if type(st.session_state.chat_logs[self.friend]) is list:
            self.display_chat_log()
            self.message_input()
        else:
            self.display_groupchat_log()
            #message_group_input(friend)
        #add_new_contact()
        #add_group_chat()

    # def loadchat(self):
    #     self.result = self.contactobj.retrieve_all()
    #     for item in self.result:
    #         st.session_state.chat_logs[item.recipient].append(item.message)


    def create_friendlist(self):
        st.sidebar.title("Friend Lists")
        friend_names = list(st.session_state.chat_logs.keys())
        self.friend = st.sidebar.radio("", friend_names)


    def display_chat_log(self):
        st.write(f"Chat history with {self.friend}:")
        for message in st.session_state.chat_logs[self.friend]:
            st.text(message.get_message())
        #display all message and new
        # result = self.contactobj.retrieve_all()
        # for item in result:
        #     if str(self.friend) == str(item.recipient):
        #         temp_mes = Message(item.message, item.timestamp)
        #         if (temp_mes in st.session_state.chat_logs[self.friend]):
        #             pass
        #         else:
        #             st.text(temp_mes.message)
        #             st.session_state.chat_logs[self.friend].append(temp_mes)

    def display_groupchat_log(self):
        st.write(f"Group history of {self.friend}:")
        contect_dic = st.session_state.group_chat[self.friend]
        #receive message
        for item in contect_dic:
            if len(contect_dic[item])>=1:
                st.write(f'{item} said:')
                for itme2 in contect_dic[item]:
                    st.text(itme2.get_message())
    
    def message_input(self):
        with st.container():
            message_input = st.text_input("Type your message here...", key="message_input")
            message_time = time.time()
            if st.button("Send", key="send"):
                if message_input:
                    message_to_send = Message(message_input, message_time)
                    st.session_state.chat_logs[self.friend].append(message_to_send)
                    self.contactobj.send(message_input, self.friend)
                    print(st.session_state.chat_logs[self.friend])
                    self.display_chat_log()

    def add_new_contact(self):
        with st.sidebar:
            new_contact = st.text_input("Add new contact name", key="new_contact")
            if st.button("Add Contact"):
                if new_contact:
                    if new_contact not in st.session_state.chat_logs:
                        st.session_state.chat_logs[new_contact] = []
                        temp = []
                        temp.append(new_contact)
                        new_contact = temp
                        st.sidebar.radio("", new_contact)
                    else:
                        st.sidebar.error("Contact already exists.")

    def get_new_message(self):
        self.new = self.contactobj.retrieve_new()
        for item in self.new:
            st.session_state.chat_logs[item.recipient].append(item.message)

if __name__ == "__main__":
    chat = Chat('168.235.86.101', 'VC1', 'VC')
    chat.main()
    # while True:
    #     chat.get_new_message()
    #     if chat.new:
    #         st.experimental_rerun() 
    #         #self.display_chat_log()
    #     time.sleep(3)