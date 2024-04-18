import streamlit as st

st.session_state.messages = []

def create_header():
    st.sidebar.title("Friend Lists")
    friend_names = ["sbDawei","shabiFrank"]
    for item in friend_names:
        st.sidebar.button(item)


with st.container():
    st.write('shabidawei')
    for message in st.session_state.messages:
        st.text(message)


with st.container():
    message_input = st.text_input("Type your message here...", key="message_input")
    if st.button("Send", key="send"):
        if message_input:  # 确保消息不为空
            st.session_state.messages.append(message_input)   


def main():
    create_header()


if __name__ == "__main__":
    main()
