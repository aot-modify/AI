import streamlit as st
import matplotlib.pyplot as plt

def area_of_square(side):
    return side ** 2

if 'calculation_log' not in st.session_state:
    st.session_state.calculation_log = []

st.title("Square Area Calculator")

side = st.text_input("Enter the side length:")
submit_button = st.button("Calculate Area")

if submit_button:
    if side:
        try:
            side = float(side)
            area = area_of_square(side)
            result_text = f"Square → side: {side} → area: {round(area, 2)}"
            st.session_state.calculation_log.append(result_text)
            st.success(f"The area is: {round(area, 2)}")

            # วาดสี่เหลี่ยมจัตุรัส
            fig, ax = plt.subplots()
            square = plt.Rectangle((0, 0), side, side, color='plum', edgecolor='black')
            ax.add_patch(square)
            ax.set_xlim(0, side * 1.2)
            ax.set_ylim(0, side * 1.2)
            ax.set_aspect('equal')
            ax.set_title(f"Square with side {side}")
            st.pyplot(fig)

        except ValueError:
            st.error("Please enter a valid number.")
    else:
        st.warning("Please enter the side length.")
