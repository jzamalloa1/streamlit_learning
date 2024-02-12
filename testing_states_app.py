import streamlit as st
import pandas as pd
import numpy as np

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