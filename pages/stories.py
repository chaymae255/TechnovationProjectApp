import streamlit as st
from PIL import Image, ImageDraw
import io
import base64

st.set_page_config(page_title="Success Stories", layout="wide")
st.title("Successful Stories")

# Data for the images
images = [
    {"id": 1, "path": "./assets/images/asmae.png", "title": "Asmae Boujibar", "career": "NASA Scientist", "description": "First Moroccan woman to work at NASA."},
    {"id": 2, "path": "./assets/images/sickLeave.jpeg", "title": "Imane Lahmami", "career": "Data Scientist", "description": "Overcame many challenges to pursue a tech career."},
    {"id": 3, "path": "./assets/images/asmae.png", "title": "Sara Ziani", "career": "Engineer", "description": "Inspired young girls in her village to study STEM."},
    {"id": 4, "path": "./assets/images/asmae.png", "title": "Nada Kabbaj", "career": "Entrepreneur", "description": "Started her own sustainable fashion brand."}
]
  
# Initialize session state for navigation
if "selected_story" not in st.session_state:
    st.session_state.selected_story = None

# Function to go back to the main gallery
def go_back():
    st.session_state.selected_story = None

# Function to select a story
def view_story(story_id):
    st.session_state.selected_story = story_id

# If a story is selected, show detail page
if st.session_state.selected_story is not None:
    selected = next(item for item in images if item["id"] == st.session_state.selected_story)
    st.image(selected["path"], width=200)
    st.markdown(f"### {selected['title']}")
    st.markdown(f"**Career:** {selected['career']}")
    st.markdown(f"**Description:** {selected['description']}")
    st.button("🔙 Back to stories", on_click=go_back)

# Otherwise, show gallery
else:
    num_columns = 3
    columns = st.columns(num_columns)

    for i, img in enumerate(images):
        with columns[i % num_columns]:
            # Load and circular crop image
            image = Image.open(img["path"]).convert("RGBA")
            width, height = image.size
            mask = Image.new("L", (width, height), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, width, height), fill=255)
            image.putalpha(mask)
            buf = io.BytesIO()
            image.save(buf, format="PNG")
            buf.seek(0)
            img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

            # Render image as clickable using button with unique key
            st.markdown(f'''
                <div style="text-align:center">
                    <button style="border:none;background:none;" onclick="fetch('/?story_id={img['id']}')">
                        <img src="data:image/png;base64,{img_base64}" width="100" height="100" style="border-radius:50%">
                    </button><br>
                    <strong>{img["title"]}</strong><br>{img["career"]}
                </div>
            ''', unsafe_allow_html=True)

            if st.button(f"View {img['title']}", key=f"btn_{img['id']}"):
                view_story(img["id"])
