# WE'LL BUILD AN SCROLLABLE, MESSAGE-RETAINER CHATBOT NOW
#  Mirroring user's input for this exercise
# We'll need:
    # Two message containers to display the user's and bot's message
    # A chat input widget to take user's input
    # A way to store the messages and display them as a rolling list

import streamlit as st
import pandas as pd
import numpy as np

st.title("El Bryan Plagiador")

# Initialize chat history in the session state (since at first this won't exist)
if "messages" not in st.session_state:
    st.session_state.messages = [] # Initialize them, so that if it does exist, it doesn't overwrite it (since we want to add more to this list later on)
    # st.session_state.counter = 0 # To prove that everything is being reloaded (point below)

# Display chat messages when app is rerun (click, new entry, etc) from history
# We have "role" and "content" keys per messages (dict) since this is the way we'll store them as in {"role":"user/ai", "content":"...."}
    # Contingent on the role, we'll write to that container (assistant container and user container)
for m in st.session_state.messages:

    # Each role will have its own chat_message() container
    with st.chat_message(m["role"]):
        # st.session_state.counter += 1 # To test reloading theory
        # st.markdown(st.session_state.counter)
        st.markdown(m["content"])

# It is not that they are rendered one after the other, it is that they are rendered all at once, but it seems like one after the other
    # because it is refreshing on each entry and displaying the whole thing + 1 element

# Now let's allow user entering messages through chat input
# Create prompt for user
prompt = st.chat_input("Que pasion?")
# The above code (entering of chat_input) will cause the app to be reran. On the first iteration there
# will be no message to display from line 22, so there won't be any "previous" messages to render. It will only render
# anything present in "messages" within the session_state, which happens on the secon iteration (containg only the message)
# from the first iteration

if prompt:
    with st.chat_message("user"):
        st.markdown("#"+prompt)
    # This will be displayed after the message rendering loop portion is ran. On the second iteration it will appear
    # rendered after the first message (which comes from the session_state messages loop)
        
    # Append it to the message history list object
    st.session_state.messages.append({"role":"user", "content":prompt})

    # Now add the "bot's message" as well to be added (and therefore rendered) continuously to the user's message
    bot_response = f"Echo: {prompt}"
    
    with st.chat_message("assistant"):
        st.markdown("#"+ bot_response)
    st.session_state.messages.append({"role":"assistant", "content":bot_response})