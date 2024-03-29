# Testing how to build a chat-gpt clone

import streamlit as st
import pandas as pd
import numpy as np

# Displaying pre-defined messages
with st.chat_message("assistant"): # The name will not be displayed, but will help with avatar representation
    st.write("Que onda?")
    st.line_chart(np.random.randn(30, 3)) # We can insert a graph into the container chat message

# We can also display messages based on user's input (chat entry box)
chat_input = st.chat_input("Dime que quieres")

# And if we want to write something based on chat_input:
if chat_input: 
    st.write(f"El morro dijo: {chat_input}")

# The above is not a chatbox per say, the messages do not scrollup. Rather they are replaced if a new entry is entered
# We'll build that in the mirror_bot.py script