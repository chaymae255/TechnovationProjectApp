import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# ---------- Page Config ----------
st.set_page_config(
    page_title="SheCan | Career Info",
    page_icon="🌸",
    layout="centered"
)

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff0f5, #f3e5f5);
        font-family: 'Trebuchet MS', sans-serif;
        color: #4a4a4a;
        padding: 20px;
    }
    h1 {
        text-align: center;
        color: #b03a64;
        font-size: 2.8em;
        margin-bottom: 10px;
    }
    .career-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .career-image {
        border-radius: 20px;
        margin-bottom: 20px;
        box-shadow: 0px 4px 12px rgba(176, 58, 100, 0.2);
    }
    .career-description {
        background-color: #ffffffaa;
        border-radius: 15px;
        padding: 20px;
        font-size: 1.2em;
        text-align: center;
        max-width: 600px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }
    .back-button {
        margin-top: 30px;
        background-color: #f48fb1;
        color: white;
        padding: 12px 30px;
        border: none;
        border-radius: 30px;
        text-decoration: none;
        font-weight: bold;
        box-shadow: 0px 4px 12px rgba(244, 143, 177, 0.4);
    }
    .back-button:hover {
        background-color: #ec407a;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Job Info Dictionary ----------
job_data = {
    "Mechanic": {
        "title": "Mechanical engineer 👩‍⚕️",
        "description": "Doctors help people stay healthy, treat illnesses, and bring hope to lives every day. It’s a noble, impactful, and rewarding career path.",
        "image": "./assets/images/she.png"
    },
    "engineer": {
        "title": "Engineer 🛠️",
        "description": "Engineers use science, creativity, and technology to solve real-world problems. They build bridges, machines, apps — and futures.",
        "image": "./assets/jobs/engineer.png"
    },
    "teacher": {
        "title": "Teacher 📚",
        "description": "Teachers shape the future by inspiring minds, encouraging growth, and spreading knowledge. They are the heart of change.",
        "image": "./assets/jobs/teacher.png"
    },
    # Add more as needed...
}


# ---------- Visualisation of probability ----------

if "probabilities" in st.session_state: 
    probabilities = st.session_state.get("probabilities")
    class_labels = st.session_state.get("class_labels")
    prob_df = pd.DataFrame(probabilities, columns=class_labels)
    prob_df = prob_df.transpose()  # Transpose to get job titles on the y-axis
    prob_df.columns = ['Probability (%)']
    prob_df['Probability (%)'] = prob_df['Probability (%)'] * 100  # Convert to percentage
    prob_df = prob_df.sort_values('Probability (%)', ascending=False)
   
    col1, col2 = st.columns([1, 2])  # Create three columns to center the image

     
    # Show the most likely job profession
    most_likely_job = prob_df.idxmax()[0]  # Get the job profession with the highest probability
    st.subheader(f"The most likely job for you is: {most_likely_job} with {prob_df.max()[0]:.2f}% probability.")
  
    
    with col1:
        # ------Pie chart
        # Select top 5 jobs to avoid clutter
        top_probs = prob_df.head(5)
        fig, ax = plt.subplots()
        ax.pie(
            top_probs['Probability (%)'], 
            labels=top_probs.index, 
            autopct='%1.1f%%', 
            startangle=140,
            colors=plt.cm.Paired.colors
        )
        ax.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle.
        st.pyplot(fig)

    #st.subheader("How each job matches your profile:")
    # for job, prob in prob_df['Probability (%)'].head(10).items():
    #     st.markdown(f"**{job}**")
    #     st.progress(int(prob))

    with col2:
    # ----Donut chart
        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(
            top_probs['Probability (%)'], 
            labels=top_probs.index, 
            autopct='%1.1f%%', 
            startangle=140,
            colors=plt.cm.Set3.colors,
            wedgeprops=dict(width=0.4)
        )
        ax.axis('equal')
        st.pyplot(fig)

    
    #----how each skill influence the choice
    skills = ['Linguistic', 'Musical', 'Bodily', 'Logical - Mathematical', 
            'Spatial-Visualization', 'Interpersonal', 'Intrapersonal', 'Naturalist']
    values = st.session_state.get("user_skills", [10]*8)  # fallback to default
    fig = go.Figure(data=go.Scatterpolar(
            r=values,
            theta=skills,
            fill='toself',
            name='Your Profile'
        ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 20])),
        showlegend=False
        )
    st.plotly_chart(fig)

    
# ---------- Get Prediction from Session ----------
if "prediction" not in st.session_state:
    st.error("No prediction found. Please take the test first.")
    st.stop()

job_key = st.session_state["prediction"][0]
st.title(job_key)

job = job_data.get(job_key)



# ---------- Display Job Info ----------
if job:
    # Title - centered
    st.markdown(f"<h1 style='color:#b03a64; text-align: center;'>{job['title']}</h1>", unsafe_allow_html=True)
    # Description and back link - centered
    st.markdown(f"""
        <div class="career-description" style="font-size: 1.1em; color: #5e4b56; text-align: center; max-width: 700px; margin: 20px auto;">
            {job['description']}
        </div>
        <br>
    """, unsafe_allow_html=True)

    # Centering the image with st.image
    col1, col2, col3 = st.columns([1, 2, 1])  # Create three columns to center the image
    with col2:
        st.image(job["image"], width=300)



    # Centering the back button
    col1, col2, col3 = st.columns([1, 2, 1])  # Create three columns again for centering the button
    with col2:
        st.markdown("""
            <a href="/" class="back-button" style="text-decoration: none; font-weight: bold; color: #b03a64; text-align: center;">← Back to Home</a>
        """, unsafe_allow_html=True)



