import streamlit as st


prediction = st.session_state.get("prediction")
if prediction: 
    st.subheader(f'Predicted Job Profession: Mechanic')
    st.success(f"Predicted Career: **{prediction[0]}**")