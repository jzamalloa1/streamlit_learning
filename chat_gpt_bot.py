# WE'LL BUILD A FULL CHAT-GPT APP

import streamlit as st
import pandas as pd
import numpy as np
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

st.title("Gordolize AI")

# Request Open API key on app start
openai_api_key = st.sidebar.text_input('Enter OpenAI API Key', type='password')

# Check if it is a valid Open API key and if so, continue with app
if openai_api_key.startswith("sk-"):

    # Initiatize in session state default model
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    # Initialize [rendering] chat history to contain messages
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Initalize LLM's chat history
    if "ai_messages" not in st.session_state:
        st.session_state["ai_messages"] = []

    # Initialize LLM model
    llm = ChatOpenAI(model=st.session_state["openai_model"], 
                    temperature=0.1, streaming=True, api_key=openai_api_key)

    # Render chat messages in role containers
    for m in st.session_state["messages"]:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    # Accept and render initial user input
    prompt = st.chat_input("Como quieres que El Gordo te ilumine hoy?")

    if prompt:

        # Render to user's container
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Store in message and ai_message history session state
        st.session_state.messages.append({"role":"user", "content":prompt})

        st.session_state.ai_messages.append(
            HumanMessage(content=prompt)
            )

        # Get ChatGPT answer, render it and store it
        with st.chat_message("assistant"):
            
            # Run model with message history (ChatOpenAI by default takes in chat request, since after all is a chat model)
            #   and in streaming mode
            # Langchain streaming docs: https://python.langchain.com/docs/modules/model_io/chat/streaming
            ai_response = llm.stream(st.session_state.ai_messages)

            # Render streaming response to AI's container AND store in object to be able to add it to chat history and AI's chat history
            ai_response_content = st.write_stream(ai_response)

            # Store in message and ai_message history session state
            st.session_state.messages.append({"role":"assistant", "content": ai_response_content})

            st.session_state.ai_messages.append(
                AIMessage(content=ai_response_content)
            )

else:
    st.warning("Please enter an Open API Key to get started")