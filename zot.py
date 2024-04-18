import streamlit as st

st.session_state.messages = []


def main():
    if 'chat_logs' not in st.session_state:
        st.session_state.chat_logs = {
            "Alan": ["How's your pj2?", "sounds good", "bye"],
            "Frank": ["Hello World", "Nice to meet you"],
            "Shelly": ["Test1", "Test2"]
        }
    create_friendlist()


def create_friendlist():
    st.sidebar.title("Friend Lists")
    friend_names = list(st.session_state.chat_logs.keys())
    friend = st.sidebar.radio("", friend_names)
    display_chat_log(friend)
    message_input(friend)

def display_chat_log(friend):
    st.write(f"与 {friend} 的聊天记录：")
    for message in st.session_state.chat_logs[friend]:
        st.text(message)

def message_input(target_name):
    with st.container():
        message_input = st.text_input("Type your message here...", key="message_input")
        if st.button("Send", key="send"):
            if message_input:  # 确保消息不为空
                st.session_state.chat_logs[target_name].append(message_input)
                # st.session_state.messages.append(message_input)   




if __name__ == "__main__":
    main()
