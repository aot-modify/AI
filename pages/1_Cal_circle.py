import math
import matplotlib.pyplot as plt
import streamlit as st

def area_of_circle(radius):
    return math.pi * (radius ** 2)

if 'calculation_log' not in st.session_state:
    st.session_state.calculation_log = []

st.title("Circle Area Calculator")
radius = st.text_input("Enter the radius of the circle:")
submit_button = st.button("Calculate Area")

if submit_button:
    if radius:
        try:
            radius = float(radius)
            area = area_of_circle(radius)
            result_text = f"Circle → radius: {radius} → area: {round(area, 2)}"
            st.session_state.calculation_log.append(result_text)
            st.success(f"The area is: {round(area, 2)}")

            # วาดวงกลม
            fig, ax = plt.subplots()
            circle = plt.Circle((0, 0), radius, color='skyblue', fill=True, edgecolor='black')
            ax.add_patch(circle)
            ax.set_aspect('equal')
            ax.set_xlim(-radius*1.2, radius*1.2)
            ax.set_ylim(-radius*1.2, radius*1.2)
            ax.set_title(f"Circle with radius {radius}")
            st.pyplot(fig)

        except ValueError:
            st.error("Please enter a valid number.")
    else:
        st.warning("Please enter a radius.")
