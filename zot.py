import streamlit as st
import ds_messenger
import time

contactobj = ds_messenger.DirectMessenger('168.235.86.101','VC1', 'VC')


def main():
    if 'chat_logs' not in st.session_state:
        st.session_state.chat_logs = {
            "Alan": ["How's your pj2?", "sounds good", "bye"],
            "Frank": ["Hello World", "Nice to meet you"],
            "SuperHammerD": ["Test1", "Test2"]
        }
    create_friendlist()

def create_friendlist():
    st.sidebar.title("Friend Lists")
    friend_names = list(st.session_state.chat_logs.keys())
    friend = st.sidebar.radio("", friend_names)
    display_chat_log(friend)
    message_input(friend)
    add_new_contact()

def display_chat_log(friend):
    st.write(f"Chat history with {friend}:")
    for message in st.session_state.chat_logs[friend]:
        st.text(message)
    result = contactobj.retrieve_all()
    for item in result:
        if str(friend) == str(item.recipient):
            st.text(item.message)
            st.session_state.chat_logs[friend].append(item.message)
    get_new_message(friend)
    
    

def message_input(target_name):
    with st.container():
        message_input = st.text_input("Type your message here...", key="message_input")
        if st.button("Send", key="send"):
            if message_input:
                st.session_state.chat_logs[target_name].append(message_input)
                contactobj.send(message_input, target_name)
                st.experimental_rerun()

def add_new_contact():
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


def get_new_message(friend):
    result2 = contactobj.retrieve_new()
    for item in result2:
        if str(friend) == str(item.recipient):
            st.text(item.message)
            st.session_state.chat_logs[friend].append(item.message)


if __name__ == "__main__":
    main()