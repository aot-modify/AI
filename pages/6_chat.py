import streamlit as st
from streamlit_chat import message
from datetime import datetime

def calculate_area(shape, inputs):
    try:
        if shape == "circle":
            r = float(inputs["radius"])
            area = 3.1416 * r ** 2
            formula = f"π × {r}² = {area:.2f}"

        elif shape == "rectangle":
            w = float(inputs["width"])
            h = float(inputs["height"])
            area = w * h
            formula = f"{w} × {h} = {area:.2f}"

        elif shape == "triangle":
            b = float(inputs["base"])
            h = float(inputs["height"])
            area = 0.5 * b * h
            formula = f"½ × {b} × {h} = {area:.2f}"

        elif shape == "square":
            s = float(inputs["side"])
            area = s ** 2
            formula = f"{s}² = {area:.2f}"

        else:
            return None, None, None

        return area, formula, img

    except:
        return None, None, None


st.set_page_config(page_title="Geometry Area ChatBot", page_icon="🧮")

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.mode = "await_shape"
    st.session_state.current_shape = ""
    st.session_state.inputs = {}

    welcome = """
👋 Welcome to Geometry Area ChatBot!

Type a shape name to calculate its area:  
**circle**, **rectangle**, **triangle**, or **square**

📌 Example:
- circle → radius: 10
- rectangle → width: 5, height: 8
- triangle → base: 6, height: 4
- square → side: 7
    """
    st.session_state.chat_history.append({"sender": "bot", "message": welcome, "timestamp": get_timestamp()})


def handle_user_input():
    user_msg = st.session_state.user_input.strip()
    st.session_state.chat_history.append({"sender": "user", "message": user_msg, "timestamp": get_timestamp()})

    if st.session_state.mode == "await_shape":
        shape = user_msg.lower()
        if shape in ["circle", "rectangle", "triangle", "square"]:
            st.session_state.current_shape = shape
            st.session_state.mode = "await_input"
            if shape == "circle":
                bot_msg = "Please enter the radius like: radius: 10"
            elif shape == "rectangle":
                bot_msg = "Please enter width and height like: width: 5, height: 8"
            elif shape == "triangle":
                bot_msg = "Please enter base and height like: base: 6, height: 4"
            elif shape == "square":
                bot_msg = "Please enter the side like: side: 7"
        else:
            bot_msg = "❗ Unsupported shape. Please enter: circle, rectangle, triangle, or square"
        st.session_state.chat_history.append({"sender": "bot", "message": bot_msg, "timestamp": get_timestamp()})

    elif st.session_state.mode == "await_input":
        inputs = {}
        parts = user_msg.split(",")
        for part in parts:
            if ":" in part:
                key, val = part.strip().split(":")
                inputs[key.strip().lower()] = val.strip()

        st.session_state.inputs = inputs
        area, formula, img = calculate_area(st.session_state.current_shape, inputs)

        if area is not None:
            bot_msg = f"""✅ **Area of {st.session_state.current_shape}**: {area:.2f} units²  
📐 **Formula**: {formula}  
<img src="{img}" width="120">"""
        else:
            bot_msg = "❌ Invalid input. Please check the format and try again."

        st.session_state.chat_history.append({"sender": "bot", "message": bot_msg, "timestamp": get_timestamp()})
        st.session_state.mode = "await_shape"
        st.session_state.current_shape = ""
        st.session_state.inputs = {}

    st.session_state.user_input = "" 


def clear_chat():
    st.session_state.chat_history = []
    st.session_state.mode = "await_shape"
    st.session_state.current_shape = ""
    st.session_state.inputs = {}

    welcome = """
👋 Welcome to Geometry Area ChatBot!

Type a shape name to calculate its area:  
**circle**, **rectangle**, **triangle**, or **square**

📌 Example:
- circle → radius: 10
- rectangle → width: 5, height: 8
- triangle → base: 6, height: 4
- square → side: 7

    """
    st.session_state.chat_history.append({"sender": "bot", "message": welcome, "timestamp": get_timestamp()})


st.title("🧮 Geometry Area ChatBot")

with st.container():
    for msg in st.session_state.chat_history:
        message(msg["message"], is_user=(msg["sender"] == "user"), allow_html=True)

st.text_input("Type your message here...", key="user_input", on_change=handle_user_input)
st.button("🔁 Start Over", on_click=clear_chat)
