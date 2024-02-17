# WE'LL BUILD A CHATBOT WITH STREAMING (LAG, DYNAMIC) CAPABILITIES

import streamlit as st
import pandas as pd
import numpy as np
import random, time

# We'll create a function to add a random "AI" response from pre-determined list
def ai_responses_generator():
    random_response = random.choice(
        [
            "Que chingados quieres ahora?",
            "Porque no le preguntas a google mejor?",
            "OK, repitemelo otra vez",
            "El Gordo esta durmiendo ahorita y no puede ayudarte"
        ]
    )

    for i in random_response.split():
        yield i + " " # Returns word by word
        time.sleep(0.05) # Adds a delay in between words (to mimic thinking/app streaming)

st.title("El Gordo")

# Initialize messages variable
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages when app is re-ran
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# Get user's input
prompt = st.chat_input("Que quieres con El Gordo?")

# Display user's response in container and add to session state
if prompt:
    # Add to user's chat container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add to session_state's message history
    st.session_state.messages.append({"role":"user", "content":prompt})

    # Render "AI"'s response and add it to the session state
    # st.write_stream() requires a generator and iterates through chunks in the sequence (therefore yield in function) 
    #  and produces a typewriter effect
    # st.write_stream() documentation at https://docs.streamlit.io/library/api-reference/write-magic/st.write_stream
    with st.chat_message("assistant"):
        ai_response = st.write_stream(ai_responses_generator())

    # Add response to session state
    st.session_state.messages.append({"role":"assistant", "content":ai_response})