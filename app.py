import streamlit as st

st.title("My First Streamlit App")
st.write("Hello Mansi ")
st.text("Let's start")

name = st.text_input("Enter name:")

if st.button("Greet"):
    st.success(f"Hello, {name}!")