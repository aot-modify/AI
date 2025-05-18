import streamlit as st

st.set_page_config(page_title="Shape Area Calculator", page_icon="🧮")

st.title("Shape Area Calculator")
st.subheader("Welcome!")
st.write(
    """
    This is a simple web app that helps you calculate the area of different shapes.
    
    👉 Use the menu on the left to navigate to the **Profile Page**, **Circle Calculator**, or other tools.
    """
)
st.markdown("---")

if 'name' in st.session_state and st.session_state.name:
    st.subheader("Submitted Names:")
    for i, person in enumerate(st.session_state.name, start=1):
        st.write(f"{i}. {person}")
else:
    st.info("No names submitted yet. Please go to the Profile Page to add names.")
