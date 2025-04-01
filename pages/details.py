import streamlit as st

# Person details
person = {
    "name": "Asmae Boujibar",
    "career": "NASA Scientist",
    "description": """
        Asmae Boujibar is a leading researcher in the field of aerospace engineering at NASA. 
        She has contributed to several key projects, including the development of advanced propulsion systems. 
        Her passion for space exploration started at a young age, and she is committed to advancing 
        the boundaries of space technology and science.
    """,
    "image_path": "./assets/asmae.png",
}

# Set page title
st.title(person["name"])

# Display the image
st.image(person["image_path"], use_container_width=True)

# Career info
st.subheader(f"Career: {person['career']}")

# Description
st.write(person["description"])

# Add a button to "Learn More" (you can link this to another page or resource)
if st.button("Learn More"):
    st.write("Redirecting to more resources about Asmae Boujibar.")
    # You can add a link or some action here, such as opening an external page
    # st.markdown('[Learn More](https://example.com)', unsafe_allow_html=True)
