import streamlit as st
import os
import json
from PIL import Image, ImageOps

# Page setup
st.set_page_config(page_title="SheCan Stories", page_icon="🌸", layout="centered")

# Custom CSS
st.markdown("""
    <style>
     .stApp {
        background: linear-gradient(to bottom right, #FFE6F0, #F3E5F5);
        font-family: 'Segoe UI', sans-serif;
        color: #4A4A4A;
    }
    .title {
        font-size: 3em;
        text-align: center;
        color: #c2185b;
        margin-bottom: 0.5em;
    }
    .subtitle {
        font-size: 1.8em;
        text-align: left;
        color: #7b1fa2;
        margin-top: 2em;
        padding-left: 20px;
    }
    .name {
        font-size: 1.3em;
        color: #ad1457;
        font-weight: bold;
        margin-top: 10px;
        text-align: center;
    }
    .summary {
    font-size: 1em;
    font-style: italic;
    color: #5e4b56;
    text-align: center;
    margin-top: 5px;
    height: 40px;            /* Fixed height */
    overflow: hidden;        /* Hide overflow */
    display: flex;
    align-items: center;
    justify-content: center;
}
    .back-link {
        text-align: center;
        margin-top: 30px;
    }
    .back-button {
        background-color: #F06292;
        color: white;
        padding: 12px 24px;
        border-radius: 30px;
        text-decoration: none;
        font-weight: bold;
        font-size: 1em;
    }
    .back-button:hover {
        background-color: #EC407A;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<div class='title'>SheCan Stories 💫</div>", unsafe_allow_html=True)

# Loop through all jobs inside 'assets'
base_path = os.getcwd()
assets_dir = os.path.join(base_path, "assets")

for job in os.listdir(assets_dir):
    job_path = os.path.join(assets_dir, job)
    story_dir = os.path.join(job_path, "stories")
   

    # Subtitle for the job
    st.markdown(f"<div class='subtitle'>{job.capitalize()} 👩‍🔧</div>", unsafe_allow_html=True)

    # Story Cards
    cols = st.columns(3)
    story_count = 0

    for i in range(1, 4):
        story_path = os.path.join(story_dir, str(i), "data.json")
        image_path = os.path.join(story_dir, str(i), "profile.png")

        if os.path.exists(story_path) and os.path.exists(image_path):
            with open(story_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            with cols[story_count % 3]:
                img = Image.open(image_path)
                img_resized = ImageOps.fit(img, (180, 180), method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
                st.image(img_resized)
                st.markdown(f"<div class='name'>{data['name']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='summary'>{data['summary']}</div>", unsafe_allow_html=True)
                with st.expander("Read More"):
                    st.markdown(data["description"])
                st.markdown("---")

            story_count += 1

# Back Button
st.markdown("""
    <div class='back-link'>
        <a href='/' class='back-button'>⬅ Back to Home</a>
    </div>
""", unsafe_allow_html=True)
