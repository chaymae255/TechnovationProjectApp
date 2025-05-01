import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# Load the saved model
model = joblib.load('./model/random_forest_model.pkl')
le = joblib.load('./model/label_encoder.pkl')

# ---------- Page Config ----------
st.set_page_config(page_title="SheCan Career Test", page_icon="🎯")

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(145deg, #fff0f5, #f3e5f5);
        font-family: 'Segoe UI', sans-serif;
    }
    
    h1, h2, h3 {
        color: #b03a64;
        text-align: center;
    }

    .stForm {
        background-color: #ffffffdd;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 4px 15px rgba(176, 58, 100, 0.2);
    }

    label {
        font-weight: bold;
        color: #5e4b56;
    }

    .stNumberInput input {
        border-radius: 10px;
    }

    .stButton>button {
        background-color: #f48fb1;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 30px;
        font-weight: bold;
        font-size: 16px;
        transition: all 0.3s ease-in-out;
    }

    .stButton>button:hover {
        background-color: #ec407a;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.title('🎯 SheCan Career Discovery Test')

# ---------- Form ----------
st.markdown("<h3>Tell us about your strengths</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#7a7a7a;'>Rate yourself from 1 to 20 on the following skills:</p>", unsafe_allow_html=True)

with st.form(key='job_form'):
    with st.container():
        linguistic = st.number_input('🗣️ How well can you express yourself through writing or speaking?', min_value=1, max_value=20, value=10)
        musical = st.number_input('🎼 How good are you at understanding and creating music?', min_value=1, max_value=20, value=10)
        bodily = st.number_input('🤸‍♀️ How good are you at using your body to express ideas or solve problems?', min_value=1, max_value=20, value=10)
        logical = st.number_input('🧠 How strong are your logical and mathematical problem-solving skills?', min_value=1, max_value=20, value=10)
        spatial = st.number_input('🎨 How good are you at visualizing shapes, sizes, and spaces in your mind?', min_value=1, max_value=20, value=10)
        interpersonal = st.number_input('🤝 How well do you work with others and understand their feelings?', min_value=1, max_value=20, value=10)
        intrapersonal = st.number_input('💖 How well do you understand your own emotions and motivations?', min_value=1, max_value=20, value=10)
        naturalist = st.number_input('🌿 How well do you understand and relate to the natural world?', min_value=1, max_value=20, value=10)

    submit_button = st.form_submit_button(label='🔍 Predict My Job')

# ---------- Prediction ----------
if submit_button:
    user_input = pd.DataFrame({
        'Linguistic': [linguistic],
        'Musical': [musical],
        'Bodily': [bodily],
        'Logical - Mathematical': [logical],
        'Spatial-Visualization': [spatial],
        'Interpersonal': [interpersonal],
        'Intrapersonal': [intrapersonal],
        'Naturalist': [naturalist]
    })

    prediction = model.predict(user_input)
    st.session_state["prediction"] = prediction
    #page_path = f"./pages/{prediction[0]}.py"
    #st.success(prediction[0])
    probabilities = model.predict_proba(user_input)
    st.session_state["probabilities"] = probabilities

    #st.success(probabilities)
    class_labels = le.classes_
    st.session_state["class_labels"] = class_labels

    #st.write(class_labels)
    #prob_df = pd.DataFrame(probabilities, columns=class_labels)
    #st.write(prob_df)
    #prob_df = prob_df.transpose()  # Transpose to get job titles on the y-axis
    #prob_df.columns = ['Probability (%)']
    #prob_df['Probability (%)'] = prob_df['Probability (%)'] * 100  # Convert to percentage
    #prob_df = prob_df.sort_values('Probability (%)', ascending=False)
    st.session_state["user_skills"] = [linguistic, musical, bodily, logical, spatial, interpersonal, intrapersonal, naturalist]
    st.switch_page("./pages/prediction.py")
    
else:
    st.warning("We don't yet have a dedicated page for your career. Check back soon!")

if st.button("stg"): 
    st.switch_page("./pages/prediction.py")
    