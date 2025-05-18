import streamlit as st
import matplotlib.pyplot as plt

def area_of_triangle(base, height):
    return 0.5 * base * height

if 'calculation_log' not in st.session_state:
    st.session_state.calculation_log = []

st.title("Triangle Area Calculator")

base = st.text_input("Enter the base:")
height = st.text_input("Enter the height:")
submit_button = st.button("Calculate Area")

if submit_button:
    if base and height:
        try:
            base = float(base)
            height = float(height)
            area = area_of_triangle(base, height)
            result_text = f"Triangle → base: {base}, height: {height} → area: {round(area, 2)}"
            st.session_state.calculation_log.append(result_text)
            st.success(f"The area is: {round(area, 2)}")

            # วาดสามเหลี่ยมมุมฉาก
            fig, ax = plt.subplots()
            triangle = plt.Polygon([[0, 0], [base, 0], [0, height]], color='salmon', edgecolor='black')
            ax.add_patch(triangle)
            ax.set_xlim(0, max(base, height) * 1.2)
            ax.set_ylim(0, max(base, height) * 1.2)
            ax.set_aspect('equal')
            ax.set_title(f"Right Triangle")
            st.pyplot(fig)

        except ValueError:
            st.error("Please enter valid numbers.")
    else:
        st.warning("Please enter both base and height.")
