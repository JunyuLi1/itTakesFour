import streamlit as st
import ds_messenger
import time

contactobj = ds_messenger.DirectMessenger('168.235.86.101','VC1', 'VC')


def main():
    if 'chat_logs' not in st.session_state:
        st.session_state.chat_logs = {
            "Alan": ["How's your pj2?", "sounds good", "bye"],
            "SuperHammerA": ["Hello World", "Nice to meet you"],
            "SuperHammerD": ["Test1", "Test2"]
        }
        st.session_state.group_chat = {}
    create_friendlist()

def create_friendlist():
    st.sidebar.title("Friend Lists")
    friend_names = list(st.session_state.chat_logs.keys())
    friend = st.sidebar.radio("", friend_names)
    if type(st.session_state.chat_logs[friend]) is list:
        display_chat_log(friend)
    else:
        display_groupchat_log(friend)
    message_input(friend)
    add_new_contact()
    add_group_chat()
    # while True:
    #     get_new_message(friend)
    #     time.sleep(3)

def display_chat_log(friend):
    st.write(f"Chat history with {friend}:")
    for message in st.session_state.chat_logs[friend]:
        st.text(message)
    result = contactobj.retrieve_all()
    for item in result:
        if str(friend) == str(item.recipient):
            st.text(item.message)
            st.session_state.chat_logs[friend].append(item.message)


def display_groupchat_log(friend):
    st.write(f"Group history of {friend}:")
    contect_dic = st.session_state.group_chat[friend]
    for item in contect_dic:
        for itme2 in contect_dic[item]:
            st.text(itme2)


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
                    st.session_state.group_chat[group_name][item] = ['test']
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
    for item in result2:
        if str(friend) == str(item.recipient):
            st.text(item.message)
            st.session_state.chat_logs[friend].append(item.message)


if __name__ == "__main__":
    main()