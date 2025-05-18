import streamlit as st

if 'name' not in st.session_state:
    st.session_state.name = []

name = st.text_input("Enter your name:")

if name and name not in st.session_state.name:
    st.session_state.name.append(name)
    st.success(f"Name '{name}' added!")

if st.session_state.name:
    st.subheader("All names submitted:")
    st.write(st.session_state.name)
