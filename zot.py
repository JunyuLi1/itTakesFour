import streamlit as st
import socket
import ds_client

st.session_state.messages = []

def create_friendlist():
    st.sidebar.title("Friend Lists")
    friend = st.sidebar.radio("", list(st.session_state.chat_logs.keys()))
    message_input(friend)
    st.write(f"Chat history with {friend}:")
    for message in st.session_state.chat_logs[friend]:
        st.text(message)


def message_input(target_name):
    with st.container():
        message_input = st.text_input("Type your message here...", key="message_input")
        if st.button("Send", key="send"):
            if message_input: # not empty
                st.session_state.chat_logs[target_name].append(message_input)
                ds_client.send('168.235.86.101', 3021, 'VC1', 'VC', message=message_input)   


def main():
    if 'chat_logs' not in st.session_state:
        st.session_state.chat_logs = {
            "Alice": ["CS121 is hard"],
            "Bob": ["Project2 is hard"],
            "Charlie": ["I can't finish pj2"]
        }
    create_friendlist()


if __name__ == "__main__":
    main()
