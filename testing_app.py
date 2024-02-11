import streamlit as st
import pandas as pd

# st.write is used to write to our app
st.write("Vamos a crear nueva data:")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)

