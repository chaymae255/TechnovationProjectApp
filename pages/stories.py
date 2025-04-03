import streamlit as st
from PIL import Image, ImageDraw
import io
import base64


st.title("successful stories")
# Define image paths
images = [
    {"path": "./assets/images/asmae.png", "title": "Asmae Boujibar", "career": "NASA", "link": "https://example.com/1"},
    {"path": "./assets/images/sickLeave.jpeg", "title": "Autre Nom", "career": "Autre Carrer", "link": "https://example.com/2"},
    {"path": "./assets/images/asmae.png", "title": "Image 1", "career": "NASA", "link": "https://example.com/3"},
    {"path": "./assets/images/asmae.png", "title": "Image 2", "career": "NASA", "link": "https://example.com/4"}
]

# Number of columns
num_columns = 3

# Create a grid
columns = st.columns(num_columns)

# Loop through images and display them in a grid
for i, img in enumerate(images):
    with columns[i % num_columns]:  # Distribute across columns
        # Open the image
        image = Image.open(img["path"])

        # Apply circular mask to image
        img_circular = image.convert("RGBA")
        width, height = img_circular.size
        mask = Image.new("L", (width, height), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, width, height), fill=255)
        img_circular.putalpha(mask)

        # Save to in-memory buffer for Streamlit to display
        buf = io.BytesIO()
        img_circular.save(buf, format="PNG")
        buf.seek(0)

        # Encode the image in base64
        img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

        # Display image as circular and clickable
        image_url = f'<a href="{img["link"]}" target="_blank"><img src="data:image/png;base64,{img_base64}" width="100" height="100" style="border-radius:50%"></a>'
        st.markdown(image_url, unsafe_allow_html=True)

        # Optionally display the title and career below the image
        st.markdown(f"**{img['title']}** - {img['career']}")
