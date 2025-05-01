import streamlit as st
import os

# ---------- Page Config ----------
st.set_page_config(
    page_title="SheCan",
    page_icon="🌸",
    layout="centered"
)

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #ffe6f0, #f3e5f5);
        font-family: 'Segoe UI', sans-serif;
        color: #4a4a4a;
    }



    h1 {
        text-align: center;
        font-size: 3em;
        color: #c2185b;
        margin-bottom: 0.2em;
    }

    .tagline {
        text-align: center;
        font-size: 1.3em;
        color: #7b1fa2;
        margin-bottom: 30px;
    }

    .description {
        font-size: 1.1em;
        color: #5e4b56;
        line-height: 1.8em;
        text-align: center;
        margin: 30px auto;
        max-width: 600px;
    }

    .arrow {
        font-size: 3em;
        text-align: center;
        margin: 10px 0 30px;
        animation: bounce 1.5s infinite;
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    .button-container {
        display: flex;
        justify-content: center;
        gap: 40px;
        flex-wrap: wrap;
        margin-bottom: 30px;
    }

    .button-custom {
        background-color: #f06292;
        color: white !important;
        padding: 14px 30px;
        font-size: 17px;
        border: none;
        border-radius: 30px;
        font-weight: 600;
        text-decoration: none !important;
        box-shadow: 0px 5px 15px rgba(240, 98, 146, 0.3);
        transition: all 0.3s ease-in-out;
    }

    .button-custom:hover {
        background-color: #ec407a;
        transform: translateY(-3px);
    }

    .button-secondary {
        background-color: #ba68c8;
    }

    .button-secondary:hover {
        background-color: #ab47bc;
    }

    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 13px;
        color: #777;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Page Content ----------

st.markdown("<h1>Welcome to SheCan 🌸</h1>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Your Future. Your Power. Your Choice.</div>", unsafe_allow_html=True)

st.markdown("""
    <div class='description'>
        SheCan is more than just a tool – it's your companion on the path to discovering who you are and what you're capable of. 
        Take a test based on your natural talents and find the career path that fits you best. 
        Or get inspired by other girls like you who dared to dream big and succeeded.
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='arrow'>👇</div>", unsafe_allow_html=True)

st.markdown("""
    <div class='button-container'>
        <a href='/test_model' target="_self" class='button-custom'>💡 Take the Test ➜</a>
        <a href='/pages/stories.py' class='button-custom button-secondary'>🌟 Success Stories ➜</a>
    </div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Made with 💖 by girls, for girls | #SheCan</div>", unsafe_allow_html=True)

st.markdown("""
    <div style="display: flex; align-items: center; justify-content: center; gap: 30px; flex-wrap: wrap;">
        <img src="assets/images/she" alt="SheCan Girl" >
        <div style="max-width: 400px; font-size: 1.1em; color: #5e4b56;">
            <p><strong>SheCan</strong> is your guide to discovering your strengths and matching them with the perfect career path. This is where dreams meet action!</p>
        </div>
    </div>
""", unsafe_allow_html=True)
st.image("./assets/images/she.png")
