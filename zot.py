import streamlit as st

friends_list = ["Friend 1", "Friend 2", "Friend 3"]
chat_history = {
    "Friend 1": [
        {"sender": "Friend 1", "message": "Hello!"},
        {"sender": "You", "message": "Hi there!"},

    ],
    "Friend 2": [
        {"sender": "You", "message": "Hey!"},
        {"sender": "Friend 2", "message": "Hi! How are you?"},
    ],
    "Friend 3": [
        {"sender": "You", "message": "Hey!"},
        {"sender": "Friend 2", "message": "Hi! How are you?"},
    ]
}
def login():
    # select different user to login
    new_user_name = st.selectbox("Select a user", friends_list, index=friends_list.index(st.session_state.selected_user_name))
    st.session_state.selected_user_name = new_user_name
    st.write("Current User:", st.session_state.selected_user_name)
    


def create_header():
    st.sidebar.title("Inbox")
    #select chat on the side
    selected_friend = st.sidebar.selectbox("Select a friend", 
    [friend for friend in list(chat_history.keys()) if friend != st.session_state.selected_user_name])
    show_chat(selected_friend)
    return selected_friend

def show_chat(selected_friend):

   #load message
    for message in chat_history.get(selected_friend, []):
        if message["sender"] == "You":
            st.write(f"You: {message['message']}")
        else:
            st.write(f"{selected_friend}: {message['message']}")

    

def send_message(friend_name, sender, message):
    global chat_history
    # Append message to friend's chat history
    chat_history[friend_name].append({"sender": sender, "message": message})
    # Append message to your chat history with the friend
    chat_history.setdefault(friend_name, []).append({"sender": sender, "message": message})

def main():
    if "selected_user_name" not in st.session_state:
        st.session_state.selected_user_name = friends_list[1]
    login()
    selected_friend = create_header()

    #sending
    message_input = st.text_input("Type a message:")
    if st.button("Send") and message_input.strip() != "":  #non empty msg
        send_message(selected_friend, "You", message_input.strip())
        show_chat(selected_friend)

    #adding friends
    add_friend_input = st.text_input("Add friend by username:")
    if st.button("Add"):
        pass
    


if __name__ == "__main__":
    main()
    #streamlit run zot.py
