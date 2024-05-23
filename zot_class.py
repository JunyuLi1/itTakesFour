import streamlit as st
import ds_messenger
from message_style import Message
import time
from streamlit_autorefresh import st_autorefresh

#{'something': {'SuperHammerA': [<message_style.Message object at 0x000002223E785910>]}}
class Chat():
    def __init__(self, ip, ucername, password):
        self.contactobj = ds_messenger.DirectMessenger(ip,ucername, password)
        self.friend = None
    def main(self):
        if 'chat_logs' not in st.session_state:
            st.session_state.chat_logs = {
                "Alan": [Message("How's your pj2?", 1), Message("sounds good", 2), Message("bye", 3)],
                "SuperHammerA": [Message("Hello World", 1), Message("Nice to meet you", 2)],
                "SuperHammerD": [Message("Test1", 1), Message("Test2", 2)]
            }
            st.session_state.group_chat = {}
        self.create_friendlist()

    def create_friendlist(self):
        st.sidebar.title("Friend Lists")
        friend_names = list(st.session_state.chat_logs.keys())
        friend = st.sidebar.radio("", friend_names)
        self.friend = friend
        if type(st.session_state.chat_logs[friend]) is list:
            self.display_chat_log(friend)
            self.message_input(friend)
        else:
            self.display_groupchat_log(friend)
            self.message_group_input(friend)
        self.add_new_contact()
        self.add_group_chat()


    def display_chat_log(self, friend):
        st.write(f"Chat history with {friend}:")
        display_log = st.empty()
        for message in st.session_state.chat_logs[friend]:
            st.text(message.get_message())
        result = self.contactobj.retrieve_all()
        for item in result:
            if str(friend) == str(item.recipient):
                temp_mes = Message(item.message, item.timestamp)
                if (temp_mes in st.session_state.chat_logs[friend]):
                    pass
                else:
                    st.text(temp_mes.message)
                    st.session_state.chat_logs[friend].append(temp_mes)


    def display_groupchat_log(self, friend):
        st.write(f"Group history of {friend}:")
        contect_dic = st.session_state.group_chat[friend]
        #receive message
        for item in contect_dic:
            if len(contect_dic[item])>=1:
                st.write(f'{item} said:')
                for itme2 in contect_dic[item]:
                    st.text(itme2.get_message())


    def message_input(self, target_name):
        with st.container():
            message_input = st.text_input("Type your message here...", key="message_input")
            message_time = time.time()
            if st.button("Send", key="send"):
                if message_input:
                    message_to_send = Message(message_input, message_time)
                    st.session_state.chat_logs[target_name].append(message_to_send)
                    self.contactobj.send(message_input, target_name)
                    st.rerun()

    def message_group_input(self, target_name):
        with st.container():
            message_input = st.text_input("Type your message here...", key="message_input")
            message_time = time.time()
            if st.button("Send", key="send"):
                if message_input:
                    message_to_send = Message(message_input, message_time)
                    st.session_state.group_chat[target_name]['user'].append(message_to_send)
                    for item in st.session_state.group_chat[target_name]: #dict
                        self.contactobj.send(message_input, item)
                    st.rerun()

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
                        st.experimental_rerun()
                    else:
                        st.sidebar.error("Contact already exists.")


    def add_group_chat(self):
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


    # def get_new_message(self, friend):
    #     result2 = self.contactobj.retrieve_new()
    #     print(result2)
    #     if len(result2) == 0:
    #         print("1234")
    #     if len(result2) != 0:
    #         for item in result2:
    #             if str(friend) == str(item.recipient):
    #                 temp_mes = Message(item.message, item.timestamp)
    #                 if (temp_mes in st.session_state.chat_logs[friend]):
    #                     pass
    #                 else:
    #                     st.text(temp_mes.message)
    #                     st.session_state.chat_logs[friend].append(temp_mes)
    #         return True
    #     else:
    #         return False
        
    # def auto_refresh(self):
    #     if self.get_new_message(self.friend):
    #         st.rerun()
    #     else:
    #         pass


if __name__ == "__main__":
    chat = Chat('168.235.86.101','SuperHammerD', '12345')
    chat.main()
    count = st_autorefresh(interval=5000, limit=100, key="data_refresh")
    #chat.auto_refresh()