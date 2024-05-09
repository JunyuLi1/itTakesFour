import streamlit as st
import ds_messenger
from message_style import Message
import time

contactobj = ds_messenger.DirectMessenger('168.235.86.101','VC1', 'VC')
#{'something': {'SuperHammerA': [<message_style.Message object at 0x000002223E785910>]}}

def main():
    if 'chat_logs' not in st.session_state:
        st.session_state.chat_logs = {
            "Alan": [Message("How's your pj2?", 1), Message("sounds good", 2), Message("bye", 3)],
            "SuperHammerA": [Message("Hello World", 1), Message("Nice to meet you", 2)],
            "SuperHammerD": [Message("Test1", 1), Message("Test2", 2)]
        }
        st.session_state.group_chat = {}
    create_friendlist()

def create_friendlist():
    st.sidebar.title("Friend Lists")
    friend_names = list(st.session_state.chat_logs.keys())
    friend = st.sidebar.radio("", friend_names)
    if type(st.session_state.chat_logs[friend]) is list:
        display_chat_log(friend)
        message_input(friend)
    else:
        display_groupchat_log(friend)
        message_group_input(friend)
    add_new_contact()
    add_group_chat()


def display_chat_log(friend):
    st.write(f"Chat history with {friend}:")
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


def display_groupchat_log(friend):
    st.write(f"Group history of {friend}:")
    contect_dic = st.session_state.group_chat[friend]
    #receive message
    for item in contect_dic:
        if len(contect_dic[item])>=1:
            st.write(f'{item} said:')
            for itme2 in contect_dic[item]:
                st.text(itme2.get_message())


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

def message_group_input(target_name):
    with st.container():
        message_input = st.text_input("Type your message here...", key="message_input")
        message_time = time.time()
        if st.button("Send", key="send"):
            if message_input:
                message_to_send = Message(message_input, message_time)
                st.session_state.group_chat[target_name]['user'].append(message_to_send)
                for item in st.session_state.group_chat[target_name]: #dict
                    contactobj.send(message_input, item)
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
                    st.experimental_rerun()
                else:
                    st.sidebar.error("Contact already exists.")


def add_group_chat():
    with st.sidebar:
        selected_contacts = st.multiselect('Select contacts to add to the group chat:', st.session_state.chat_logs)
        group_name = st.text_input('Enter a name for the group chat:', '')
        if st.button('Create Group Chat'):
            if len(selected_contacts)>=2 and group_name:
                st.session_state.group_chat[group_name] ={}
                st.session_state.chat_logs[group_name] = {}
                for item in selected_contacts:
                    st.session_state.group_chat[group_name][item] = [Message(f'Hi from {item}',1)]
                st.session_state.group_chat[group_name]['user'] = []
                print(st.session_state.group_chat)
                temp = []
                temp.append(group_name)
                new_contact = temp
                st.sidebar.radio("", new_contact)
                st.experimental_rerun()
            else:
                st.error("Please select at least two to create a group chat.")


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