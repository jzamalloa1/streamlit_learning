import streamlit as st
import pandas as pd
import numpy as np

# Notice how everything is centered in the screen, and every new element is drawn right below the previous one

# st.write is used to write to our app
st.write("Vamos a crear nueva data:")

# Create data to display
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

# Note: just printing it can also render it. So not necessarily to do st....
df

# Also, render it using the built-in streamlit dataframe function, and add styling
st.dataframe(df.style.highlight_max(axis=0)) # Highlights the maximum value in the columns (axis=0)

# You can also generate a static (non-interactive) table
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

# We can also draw figures within the app. Streamlit figures are interactive
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(data=chart_data)

# We can also incorporate widgets into it
x = st.slider("x") # Assigns the slider output to the variable x
st.write(x, "squared is", x**2) # So that it results is dynamically changed and outputted in the results

# Widgets can be accessed by their key (if you assigned one to it). If a widget has a key, it is automatically added to the session state
st.text_input("Mi nombre", key="m")
st.session_state.m #It will print out what we write in the text_input box

# Checkboxes can be used to show or hide data
if st.checkbox("Demuestrame la tabla"):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
    
    st.dataframe(chart_data)

# "Selectbox" is used to select from a series
a = pd.Series([1,2,3])

option = st.selectbox("Which number is larger", a)
"You selected: ", option 

# We can separate the structure of the page layout by adding a sidebar
selectbox_output = st.sidebar.selectbox(
    "Que personaje de One Piece te gusta mas?",
    ("Luffy", "Zoro", "Shanks")
)

slider_output = st.sidebar.slider(
    "Selecciona tu rango de bmi",
    0.0, 70.0, (25.0, 50.0) #All values must be of the same type (e.g. all floats)
)

# We can also structure it by columns - Theoretically we can place this at the top to break the whole page by two (+ sidebar)
lc, rc = st.columns(2)

lc.button("Presioname!!")

with rc:
    selected_ratio = st.radio(
        "Ganador de la Liga 1 2024",
        ("Universitario", "Alianza Lima", "Sporting Cristal", "Los Chankas")
    )
    st.write("You selected", selected_ratio)