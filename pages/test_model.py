import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the saved model
model = joblib.load('./model/random_forest_model.pkl')

# Load LabelEncoder (you should save it after training as well, if necessary)
le = LabelEncoder()
le.fit(["Astronomer", "Geologist", "Marine Biologist", "Veterinarian", "Nature photographer", 
        "Recording engineer", "Audiologist", "Sound editor", "Music teacher", "Actuary", 
        "Chartered Accountant", "Computer analyst", "Computer programmer", "Database designer", 
        "Economist", "Librarian", "Engineer", "Lawyer", "Pharmacist", "Physician", "Physicist", 
        "Mathematician", "Leader", "Manager", "Politician", "Social Worker", "Receptionist", 
        "Sales Representative", "Counselor", "Athlete", "Dancer", "Mechanic", "Actor / Actress", 
        "Physical Therapist", "Editor", "Historian", "Journalist", "Language Teacher", "Poet", 
        "Broadcaster", "Artist", "Graphic Designer", "Fashion Designer", "Interior Decorator", 
        "Pilot", "Psychologist", "Philosopher", "Writer", "Criminologist", "Company secretary", 
        "Marketing", "Logistics manager", "Research analyst", "Business manager", "Internal auditor", 
        "Chief financial officer", "Business Analyst", "Banking", "Stock Broker", "Financial Advisor", 
        "Consultant", "Archeologist", "Pre Primary Teacher", "Primary Teacher", "Middle School Teacher", 
        "Higher School Teacher", "Professor", "Anthropologist", "Medical", "Para Medical", "Military", 
        "Para Military", "Police Force", "Technician"])

# Title of the app
st.title('Job Profession Predictor')

# Collect user inputs (competency scores)
st.header("Enter your skills/competencies:")

linguistic = st.slider('Linguistic Ability', 1, 20, 10)
musical = st.slider('Musical Ability', 1, 20, 10)
bodily = st.slider('Bodily-Kinesthetic Ability', 1, 20, 10)
logical = st.slider('Logical-Mathematical Ability', 1, 20, 10)
spatial = st.slider('Spatial-Visualization Ability', 1, 20, 10)
interpersonal = st.slider('Interpersonal Ability', 1, 20, 10)
intrapersonal = st.slider('Intrapersonal Ability', 1, 20, 10)
naturalist = st.slider('Naturalist Ability', 1, 20, 10)

# Create a DataFrame for the input values
input_data = pd.DataFrame({
    'Linguistic': [linguistic],
    'Musical': [musical],
    'Bodily': [bodily],
    'Logical - Mathematical': [logical],
    'Spatial-Visualization': [spatial],
    'Interpersonal': [interpersonal],
    'Intrapersonal': [intrapersonal],
    'Naturalist': [naturalist]
})

# Make prediction using the trained model
prediction = model.predict(input_data)

# Decode the prediction to the actual job profession
predicted_job = le.inverse_transform(prediction)

# Display the prediction result
st.subheader(f'Predicted Job Profession: {predicted_job[0]}')
