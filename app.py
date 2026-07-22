import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq Chat endpoint
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

# Function to get response from Groq API
def ask_groq_chat(chat_history):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-oss-20b",
        "messages": chat_history
    }

    try:
        response = requests.post(GROQ_URL, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="Football Chatbot", page_icon="⚽", layout="wide")

# Custom CSS for ChatGPT-style UI
st.markdown("""
<style>
body {
    background-color: #0B0C10;
    color: #FFFFFF;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
h1 {
    text-align: center;
    color: #FFFFFF;
    margin-bottom: 0px;
}
h3 {
    color: #FFFFFF;
}
p {
    text-align: center;
    color: #B0B0B0;
}
.chat-container {
    max-height: 70vh;
    overflow-y: auto;
    padding: 10px;
    margin-bottom: 10px;
}
.user-message {
    background-color: #4CAF50;
    color: white;
    padding: 12px;
    border-radius: 12px;
    width: fit-content;
    max-width: 60%;
    margin-left: auto;
    margin-bottom: 8px;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.3);
}
.bot-message {
    background-color: #1F1F1F;
    color: white;
    padding: 12px;
    border-radius: 12px;
    width: fit-content;
    max-width: 60%;
    margin-right: auto;
    margin-bottom: 8px;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.3);
}
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background-color: #4CAF50;
    border-radius: 4px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚽ Football Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p>Ask anything about football: latest news, players, teams, stats, etc.</p>", unsafe_allow_html=True)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat container
chat_container = st.container()

# Input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input(
        label="Your Message",  # non-empty label
        placeholder="Type your message here...",
        label_visibility="hidden"  # hide it from UI
    )
    submit_button = st.form_submit_button("Send")

if submit_button and user_input.strip() != "":
    # Add user message to history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Get assistant response
    with st.spinner("Thinking..."):
        assistant_reply = ask_groq_chat(st.session_state.chat_history)

    # Add assistant message to history
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_reply})

# Display chat messages
with chat_container:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(f'<div class="user-message"><b>You:</b> {chat["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-message"><b>Bot:</b> {chat["content"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
