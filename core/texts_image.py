import streamlit as st
from pathlib import Path
import base64

# Text&Image Functions
def texto(text, size, color):
    st.markdown(f'<p font-weight:normal; style="font-size:{size}px;color:{color};text-align:justify;">{text}</p>',
        unsafe_allow_html=True)

def texto2(text, size, color):
    st.markdown(f'<p font-weight:normal; style="font-size:{size}px;color:{color};text-align:center;">{text}</p>',
        unsafe_allow_html=True)


def title(text, size, color):
    st.markdown(f'<h1 font-weight:normal; style="font-size:{size}px;color:{color};text-align:center;">{text}</h1>',
                unsafe_allow_html=True)
    return


def title2(text):
    st.markdown(f'<h1 font-weight:normal; style="font-size:20px;color:"black";text-align:justify;">{text}</h1>',
                unsafe_allow_html=True)
    return


def img_bytes(path):
    img_bytes = Path(path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded