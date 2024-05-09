import streamlit as st
import ds_messenger
from message_style import Message
from streamlit_autorefresh import st_autorefresh
import time

contactobj = ds_messenger.DirectMessenger('168.235.86.101','SuperHammerD', '12345')


def main():
    if 'chat_logs' not in st.session_state:
        st.session_state.chat_logs = {
            "VC1": [Message("How's your pj2?", 1), Message("sounds good", 2), Message("bye", 3)],
            "SuperHammerA": [Message("Hello World", 1), Message("Nice to meet you", 2)],
            "SuperHammerD": [Message("Test1", 1), Message("Test2", 2)]
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
    display_log = st.empty()
    for message in st.session_state.chat_logs[friend]:
        st.text(message.get_message())
    result = contactobj.retrieve_all()
    for item in result:
        if str(friend) == str(item.recipient):
            temp_mes = Message(item.message, item.timestamp)
            if (temp_mes in st.session_state.chat_logs[friend]):
                pass
            else:
                st.text(temp_mes.message)
                st.session_state.chat_logs[friend].append(temp_mes)
    #display_log.text("\n".join(st.session_state.chat_logs[friend]))
        
    

def message_input(target_name):
    with st.container():
        message_input = st.text_input("Type your message here...", key="message_input")
        message_time = time.time()
        if st.button("Send", key="send"):
            if message_input:
                message_to_send = Message(message_input, message_time)
                st.session_state.chat_logs[target_name].append(message_to_send)
                contactobj.send(message_input, target_name)
                st.rerun()

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
    if result2 != None:
        for item in result2:
            if str(friend) == str(item.recipient):
                temp_mes = Message(item.message, item.timestamp)
                if (temp_mes in st.session_state.chat_logs[friend]):
                    pass
                else:
                    st.text(temp_mes.message)
                    st.session_state.chat_logs[friend].append(temp_mes)
        return True
    else:
        return False


if __name__ == "__main__":
    main()