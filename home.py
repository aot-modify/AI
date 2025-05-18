import streamlit as st

st.set_page_config(
    page_title="Shape Area Calculator",
    page_icon="🧮",
)

st.title("🧮 Shape Area Calculator")
st.subheader("Welcome!")
st.write(
    """
    This is a simple web app that helps you calculate the area of different shapes.
    
    👉 Use the menu on the left to navigate to the **Circle Calculator** or other shape calculators.
    """
)
st.markdown("---")

if 'name' in st.session_state:
    st.write(f"Hello + {st.session_state.name}")

if 'name' not in st.session_state:
    st.session_state.name.append(name)
    st.write(name)