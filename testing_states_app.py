import streamlit as st
import pandas as pd
import numpy as np

# Check the session state
if "counter" not in st.session_state: #If not in session state, initialize it. 
    # Theoretically this will be initialized when refresh, will be different for different users, and different in different tabs
    st.session_state.counter = 0

st.session_state.counter += 1 # Add one every time we run it again

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")   

st.markdown("""So the session will be run everytime the user interacts with the page (script).
         If the user clicks a button (selectbox, radio, etc), then the counter will increase
         (page runs once more) since the 'counter' key already exists in the session state (initialized).
         The session state will only be reset when the page is refreshed, a new tab is open, and
         will be different for different users.""")

# Add Title
st.header("Testing States in Streamlit", divider="rainbow")

# Break page into left and right columns
lc, rc = st.columns(2, gap="medium")

with lc:
    st.subheader("Left column")

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
        )

    st.line_chart(data=chart_data)

with rc:
    st.subheader("Right column")
    st.write("This is the right side")

# Add sidebar
with st.sidebar:
    sb_output = st.selectbox(
        "Que personaje de One Piece te gusta mas?",
        ("Luffy", "Zoro", "Shanks"),
        index=None,
        placeholder="Selecciona uno guey"
    )