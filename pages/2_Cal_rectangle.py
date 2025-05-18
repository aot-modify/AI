import streamlit as st
import matplotlib.pyplot as plt

def area_of_rectangle(length, width):
    return length * width

if 'calculation_log' not in st.session_state:
    st.session_state.calculation_log = []

st.title("Rectangle Area Calculator")

length = st.text_input("Enter the length:")
width = st.text_input("Enter the width:")
submit_button = st.button("Calculate Area")

if submit_button:
    if length and width:
        try:
            length = float(length)
            width = float(width)
            area = area_of_rectangle(length, width)
            result_text = f"Rectangle → length: {length}, width: {width} → area: {round(area, 2)}"
            st.session_state.calculation_log.append(result_text)
            st.success(f"The area is: {round(area, 2)}")

            # วาดรูป
            fig, ax = plt.subplots()
            rect = plt.Rectangle((0, 0), width, length, color='lightgreen', edgecolor='black')
            ax.add_patch(rect)
            ax.set_xlim(0, max(width, length) * 1.2)
            ax.set_ylim(0, max(width, length) * 1.2)
            ax.set_aspect('equal')
            ax.set_title(f"Rectangle {length} x {width}")
            st.pyplot(fig)

        except ValueError:
            st.error("Please enter valid numbers.")
    else:
        st.warning("Please enter both values.")
