import streamlit as st
from nltk.chat.util import Chat, reflections
from instructed_chatbot import pairs

chat = Chat(pairs, reflections)

st.set_page_config(page_title="Instructed Chatbit", page_icon="🤖")

st.title(" 🤖  Simple Instructed Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot** {msg['content']}")

user_input = st.chat_input("Start chatting here....")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = chat.respond(user_input)
    if response:
        st.session_state.messages.append({"role": "bot", "content": response})
    else:
        st.session_state.messages.append(
            {"role": "bot", "content": "i didn't understand boss"}
        )

    st.rerun()
