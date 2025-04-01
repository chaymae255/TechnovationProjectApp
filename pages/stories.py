import streamlit as st

# Define image paths
images = [
    {"path": "./assets/asmae.png", "title": "asmae boujibar","career":"NASA", "link": "https://example.com/1"},
    {"path": "./assets/asmae.png", "title": "Image 1","career":"NASA", "link": "https://example.com/1"},
    {"path": "./assets/asmae.png", "title": "Image 1","career":"NASA", "link": "https://example.com/1"}

]

# Number of columns
num_columns = 3

# Create a grid
columns = st.columns(num_columns)

# Loop through images and display them in a grid
for i, img in enumerate(images):
    with columns[i % num_columns]:  # Distribute across columns
        st.image(img["path"], use_container_width=True, caption=img["title"]+":"+img["career"] )  # ✅ Updated to use_container_width
        if st.button(f"View More {i+1}", key=f"btn_{i}"):  # Unique key for each button
            st.write(f"Redirecting to {img['link']}") 