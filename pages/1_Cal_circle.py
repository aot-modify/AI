import math
import streamlit as st
#print("Hello CTH")

# area of  square
# def square(x):
#     return x * x
# result = square(5)
# print(f"the area is {result}")

# area of circle
def area_of_circle(radius):
    return math.pi * (radius ** 2)
#result = area_of_circle(5)
#print(f"the area is {round(result, 2)}")

st.title("Shape Area Calculator")
st.write("This app calculates the area of different shapes.")

radius = st.text_input("Enter the radius of the circle:")
submit_button = st.button("Calculate Area")
if submit_button:
    if radius:
        try:
            radius = float(radius)
            area = area_of_circle(radius)
            st.write(f"The area of the circle with radius {radius} is: {round(area, 2)}")
        except ValueError:
            st.write("Please enter a valid number for the radius.")
    else:
        st.write("Please enter a radius to calculate the area.")

