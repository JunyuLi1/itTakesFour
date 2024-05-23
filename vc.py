import streamlit as st
import ds_messenger
import time
from collections import defaultdict

class Chat:
    def __init__(self, ip, vc1, vc):
        self.contactobj = ds_messenger.DirectMessenger(ip, vc1, vc)
        st.session_state.chat_logs = defaultdict(list)
        self.friend = None
        self.result = None
        self.new = None

    def main(self):
        self.loadchat()
        self.create_friendlist()
        self.display_chat_log()
        self.message_input()
        self.add_new_contact()
        while True:
            self.get_new_message()
            if self.new:
                st.experimental_rerun() 
                self.display_chat_log()
            time.sleep(3)

    def loadchat(self):
        self.result = self.contactobj.retrieve_all()
        for item in self.result:
            st.session_state.chat_logs[item.recipient].append(item.message)


    def create_friendlist(self):
        st.sidebar.title("Friend Lists")
        friend_names = list(st.session_state.chat_logs.keys())
        self.friend = st.sidebar.radio("", friend_names)


    def display_chat_log(self):
        st.write(f"Chat history with {self.friend}:")
        for message in st.session_state.chat_logs[self.friend]:
            st.text(message)


    def message_input(self):
        with st.container():
            message_input = st.text_input("Type your message here...", key="message_input")
            if st.button("Send", key="send"):
                if message_input:
                    st.session_state.chat_logs[self.friend].append(message_input)
                    self.contactobj.send(message_input, self.friend)
                    st.experimental_rerun()

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
    while True:
        chat.get_new_message()
        if chat.new:
            st.experimental_rerun() 
            #self.display_chat_log()
        time.sleep(3)