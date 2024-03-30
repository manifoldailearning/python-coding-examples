#https://docs.streamlit.io/library/cheatsheet

import streamlit as st

st.title("Title for our Streamlit app ")

st.header("Heading of Streamlit app")

st.subheader('Sub-headding of streamlit')

st.text("This is an example text")

st.success("Success message")

st.warning("Warning message")

st.error("error message")

if st.checkbox("Select/Unselect"):
    st.text("User selected checkbox")

else:
    st.error("Checkbox not selected")

state = st.radio("What is your favorite color ?", ['Red','Green','Yellow'])

if state=='Green':
    st.success("Thats my favorite color as well")

occupation = st.selectbox("What do you do?",['Student','Professional','Trainer','Vlogger'])

st.text(f"selected option is {occupation}")

st.multiselect("Buy", ["milk", "apples", "potatoes"])

if st.button("Click me"):
    st.success("Button clicked")
    
st.sidebar.header("Heading of sidebar")