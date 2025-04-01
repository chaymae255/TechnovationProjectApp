import streamlit as st

# Form for gathering user input
with st.form("user_form"):
    # Form fields
    name = st.text_input("Your Name")
    age = st.number_input("Your Age", min_value=1, max_value=100)
    gender = st.radio("Select Gender", ["Male", "Female", "Other"])
    feedback = st.text_area("Your Feedback")
    
    # Form submission button
    submit_button = st.form_submit_button("Submit")
    
# Display the results after submission
if submit_button:
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Gender: {gender}")
    st.write(f"Feedback: {feedback}")

if st.button("Go Back to Home"):
    st.switch_page("streamlit_app.py")