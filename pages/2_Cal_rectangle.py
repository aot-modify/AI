import math
import streamlit as st

# area of circle
def area_of_ractangle(length, width):
    return length * width

st.title("Shape Area Calculator")  
st.write("This app calculates the area of different shapes.")

length = st.text_input("Enter the length of the rectangle:")
width = st.text_input("Enter the width of the rectangle:")
submit_button = st.button("Calculate Area")
if submit_button:
    if length and width:
        try:
            length = float(length)
            width = float(width)
            area = area_of_ractangle(length, width)
            st.write(f"The area of the rectangle with length {length} and width {width} is: {round(area, 2)}")
        except ValueError:
            st.write("Please enter valid numbers for the length and width.")
    else:
        st.write("Please enter both length and width to calculate the area.")

