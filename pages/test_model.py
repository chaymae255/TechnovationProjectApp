import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the saved model
model = joblib.load('./model/random_forest_model.pkl')

# Load the LabelEncoder
le = joblib.load('./model/label_encoder.pkl')

# Title of the app
st.title('Job Profession Predictor')

# Collect user inputs (competency scores)
st.header("On a scale of 1 to 20:")

with st.form(key='job_form'):
    linguistic = st.number_input('how well can you express yourself through writing or speaking?', min_value=1, max_value=20, value=10)
    musical = st.number_input('how good are you at understanding and creating music?', min_value=1, max_value=20, value=10)
    bodily = st.number_input('how good are you at using your body to express ideas or solve problems?', min_value=1, max_value=20, value=10)
    logical = st.number_input('how strong are your logical and mathematical problem-solving skills?', min_value=1, max_value=20, value=10)
    spatial = st.number_input('how good are you at visualizing shapes, sizes, and spaces in your mind?', min_value=1, max_value=20, value=10)
    interpersonal = st.number_input('how well do you work with others and understand their feelings?', min_value=1, max_value=20, value=10)
    intrapersonal = st.number_input('how well do you understand your own emotions and motivations?', min_value=1, max_value=20, value=10)
    naturalist = st.number_input('how well do you understand and relate to the natural world?', min_value=1, max_value=20, value=10)
    
    submit_button = st.form_submit_button(label='Predict Job Profession')

# Predict when form is submitted
if submit_button:
    # Store the user input in a DataFrame
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

    # Make the prediction using the trained model
    prediction = model.predict(user_input)
    st.session_state["prediction"] = prediction
    st.switch_page("./pages/prediction.py")
    # Display the prediction result
    

