import streamlit as st


prediction = st.session_state.get("prediction")
if prediction: 
    st.subheader(f'Predicted Job Profession: {prediction[0]}')
    st.success(f"Predicted Career: **{prediction[0]}**")