import streamlit as st

st.session_state.messages = []

# st.session_state.chat_logs = {
#         "Alice": ["你好，Alice！", "最近怎么样？", "听说你去旅行了！"],
#         "Bob": ["嘿，Bob，周末打算做什么？", "我们去徒步如何？"],
#         "Charlie": ["Charlie，下次聚会你准备带些什么？", "我可以带些饮料。"]
#     }


def create_friendlist():
    st.sidebar.title("Friend Lists")
    friend_names = ["sbDawei","shabiFrank"]
    friend = st.sidebar.radio("", list(st.session_state.chat_logs.keys()))
    message_input(friend)
    st.write(f"与 {friend} 的聊天记录：")
    for message in st.session_state.chat_logs[friend]:
        st.text(message)

def load_chat_history(friend):
    pass

def message_input(target_name):
    with st.container():
        message_input = st.text_input("Type your message here...", key="message_input")
        if st.button("Send", key="send"):
            if message_input:  # 确保消息不为空
                st.session_state.chat_logs[target_name].append(message_input)
                # st.session_state.messages.append(message_input)   


def main():
    if 'chat_logs' not in st.session_state:
        st.session_state.chat_logs = {
            "Alice": ["你好，Alice！", "最近怎么样？", "听说你去旅行了！"],
            "Bob": ["嘿，Bob，周末打算做什么？", "我们去徒步如何？"],
            "Charlie": ["Charlie，下次聚会你准备带些什么？", "我可以带些饮料。"]
        }
    create_friendlist()


if __name__ == "__main__":
    main()
