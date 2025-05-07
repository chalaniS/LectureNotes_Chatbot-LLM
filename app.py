# app.py
import streamlit as st
from chatbot import ask  # Importing the ask function from chatbot.py

# Set up page
st.set_page_config(page_title="CTSE Chatbot", layout="wide")
st.title("📘 CTSE Lecture Notes Chatbot (Llama3 + LangChain)")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
with st.form("chat_form", clear_on_submit=True):
    user_query = st.text_input("Ask a question about CTSE or Software Engineering:", key="user_input")
    submit = st.form_submit_button("Ask")

# Process the user query
if submit and user_query:
    try:
        with st.spinner("🤖 Thinking..."):
            answer = ask(user_query)
        # Save Q&A to history
        st.session_state.chat_history.append(("You", user_query))
        st.session_state.chat_history.append(("Bot", answer))
    except Exception as e:
        st.session_state.chat_history.append(("Bot", f"⚠️ Error: {str(e)}"))

# Display chat history
# for role, msg in st.session_state.chat_history:
#     if role == "You":
#         st.markdown(f"**🧑 {role}:** {msg}")
#     else:
#         st.markdown(f"**🤖 {role}:** {msg}")

# Chat display area as a scrollable stack
st.markdown("""
    <style>
    .chat-container {
        max-height: 500px;
        overflow-y: auto;
        padding: 10px;
        background-color: #fafafa;
        border: 1px solid #ddd;
        border-radius: 10px;
    }
    .chat-message {
        margin-bottom: 10px;
        padding: 10px;
        border-radius: 10px;
    }
    .chat-user {
        background-color: #DCF8C6;
        text-align: right;
    }
    .chat-bot {
        background-color: #F1F0F0;
    }
    </style>
    <div class="chat-container">
""", unsafe_allow_html=True)

# Display chat messages in stacked order
for role, msg in st.session_state.chat_history:
    if role == "You":
        st.markdown(
            f"<div class='chat-message chat-user'><strong>🧑 {role}:</strong> {msg}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='chat-message chat-bot'><strong>🤖 {role}:</strong> {msg}</div>",
            unsafe_allow_html=True
        )

# Close container div
st.markdown("</div>", unsafe_allow_html=True)

