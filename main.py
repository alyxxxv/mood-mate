import streamlit as st
from pages.chatbot import chatbot
from pages.screaning import screaning
from pages.psikolog import psikolog
pages = {
    "Chatbot" : chatbot,
    "screaning" : screaning,
    "psikolog" : psikolog
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages))

page = pages[selection]
page()