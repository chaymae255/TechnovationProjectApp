import streamlit as st

st.title("technovation")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
if st.button("Go to Form Page"):
    st.switch_page("./pages/form.py")

if st.button("Go to stories Page"):
    st.switch_page("./pages/stories.py")