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
  s
    </style>
""", unsafe_allow_html=True)


# ---------- Visualisation of probability ----------

if "probabilities" in st.session_state: 
    probabilities = st.session_state.get("probabilities")
    class_labels = st.session_state.get("class_labels")
    prob_df = pd.DataFrame(probabilities, columns=class_labels)
    prob_df = prob_df.transpose()  # Transpose to get job titles on the y-axis
    prob_df.columns = ['Probability (%)']
    prob_df['Probability (%)'] = prob_df['Probability (%)'] * 100  # Convert to percentage
    prob_df = prob_df.sort_values('Probability (%)', ascending=False)
   
    
     
    # Show the most likely job profession
    most_likely_job = prob_df.idxmax()[0]  # Get the job profession with the highest probability
    st.subheader(f"The most likely job for you is: {most_likely_job} with {prob_df.max()[0]:.2f}% probability.")
  
    col1, col2 = st.columns(2)  # Create three columns to center the image
    with col1:
        # ------Pie chart
        # Select top 5 jobs to avoid clutter
        top_probs = prob_df.head(5)
        fig, ax = plt.subplots(figsize=(4, 4))  # Make it square and smaller
        ax.pie(
            top_probs['Probability (%)'], 
            labels=top_probs.index, 
            autopct='%1.1f%%', 
            startangle=140,
            colors=plt.cm.Paired.colors
        )
        ax.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle.
        st.pyplot(fig, clear_figure=True)

    #st.subheader("How each job matches your profile:")
    # for job, prob in prob_df['Probability (%)'].head(10).items():
    #     st.markdown(f"**{job}**")
    #     st.progress(int(prob))

    with col2:
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
        showlegend=False,
        autosize=False,
        width=300,
        height=300,  # Match to matplotlib figure
       #margin=dict(l=40, r=40, t=40, b=40)  # Reduce margin to align visually
    )
        st.plotly_chart(fig)
    

# ---------- Job Info Dictionary ----------
job_data = {
    "astronomer": {
        "title": "Astronomer 🌌",
        "description": "Astronomers study celestial objects and phenomena, exploring the origins and evolution of the universe.",
        "image": "./assets/jobs/astronomer.png"
    },
    "geologist": {
        "title": "Geologist 🪨",
        "description": "Geologists analyze Earth's materials, structures, and processes to understand its history and predict future changes.",
        "image": "./assets/jobs/geologist.png"
    },
    "marine_biologist": {
        "title": "Marine Biologist 🐠",
        "description": "Marine biologists research ocean ecosystems, studying marine organisms and their interactions with the environment.",
        "image": "./assets/jobs/marine_biologist.png"
    },
    "veterinarian": {
        "title": "Veterinarian 🐾",
        "description": "Veterinarians diagnose and treat health issues in animals, ensuring their well-being and preventing disease spread.",
        "image": "./assets/jobs/veterinarian.png"
    },
    "nature_photographer": {
        "title": "Nature Photographer 📷",
        "description": "Nature photographers capture the beauty of the natural world, highlighting wildlife and landscapes through imagery.",
        "image": "./assets/jobs/nature_photographer.png"
    },
    "recording_engineer": {
        "title": "Recording Engineer 🎚️",
        "description": "Recording engineers manage the technical aspects of audio recording, ensuring high-quality sound production.",
        "image": "./assets/jobs/recording_engineer.png"
    },
    "audiologist": {
        "title": "Audiologist 👂",
        "description": "Audiologists specialize in diagnosing and treating hearing and balance disorders, improving patients' auditory health.",
        "image": "./assets/jobs/audiologist.png"
    },
    "sound_editor": {
        "title": "Sound Editor 🎧",
        "description": "Sound editors assemble and refine audio tracks for media productions, enhancing the overall auditory experience.",
        "image": "./assets/jobs/sound_editor.png"
    },
    "music_teacher": {
        "title": "Music Teacher 🎼",
        "description": "Music teachers educate students in music theory and practice, fostering musical skills and appreciation.",
        "image": "./assets/jobs/music_teacher.png"
    },
    "actuary": {
        "title": "Actuary 📊",
        "description": "Actuaries analyze financial risks using mathematics and statistics to aid in decision-making processes.",
        "image": "./assets/jobs/actuary.png"
    },
    "chartered_accountant": {
        "title": "Chartered Accountant 💼",
        "description": "Chartered accountants manage financial records, audits, and tax matters, ensuring fiscal responsibility.",
        "image": "./assets/jobs/chartered_accountant.png"
    },
    "computer_analyst": {
        "title": "Computer Analyst 🖥️",
        "description": "Computer analysts evaluate and improve computer systems, enhancing organizational efficiency.",
        "image": "./assets/jobs/computer_analyst.png"
    },
    "computer_programmer": {
        "title": "Computer Programmer 💻",
        "description": "Computer programmers write and test code that enables software applications to function effectively.",
        "image": "./assets/jobs/computer_programmer.png"
    },
    "database_designer": {
        "title": "Database Designer 🗄️",
        "description": "Database designers create structured data storage systems, facilitating efficient data retrieval and management.",
        "image": "./assets/jobs/database_designer.png"
    },
    "economist": {
        "title": "Economist 📈",
        "description": "Economists study economic trends and data to advise on policy and business strategies.",
        "image": "./assets/jobs/economist.png"
    },
    "librarian": {
        "title": "Librarian 📚",
        "description": "Librarians manage information resources, assisting patrons in accessing and utilizing various materials.",
        "image": "./assets/jobs/librarian.png"
    },
    "engineer": {
        "title": "Engineer 🛠️",
        "description": "Engineers apply scientific principles to design and build structures, machines, and systems.",
        "image": "./assets/jobs/engineer.png"
    },
    "lawyer": {
        "title": "Lawyer ⚖️",
        "description": "Lawyers provide legal advice, represent clients in court, and draft legal documents.",
        "image": "./assets/jobs/lawyer.png"
    },
    "pharmacist": {
        "title": "Pharmacist 💊",
        "description": "Pharmacists dispense medications and counsel patients on their proper use and potential side effects.",
        "image": "./assets/jobs/pharmacist.png"
    },
    "physician": {
        "title": "Physician 🩺",
        "description": "Physicians diagnose and treat illnesses, promoting overall health and wellness.",
        "image": "./assets/jobs/physician.png"
    },
    "physicist": {
        "title": "Physicist 🧪",
        "description": "Physicists explore the laws of nature, conducting experiments to understand physical phenomena.",
        "image": "./assets/jobs/physicist.png"
    },
    "mathematician": {
        "title": "Mathematician ➗",
        "description": "Mathematicians develop theories and solve problems using mathematical techniques.",
        "image": "./assets/jobs/mathematician.png"
    },
    "leader": {
        "title": "Leader 🧭",
        "description": "Leaders guide organizations or groups towards achieving goals through strategic decision-making.",
        "image": "./assets/jobs/leader.png"
    },
    "manager": {
        "title": "Manager 📋",
        "description": "Managers oversee operations and teams, ensuring productivity and goal attainment.",
        "image": "./assets/jobs/manager.png"
    },
    "politician": {
        "title": "Politician 🏛️",
        "description": "Politicians represent the public, crafting policies and making decisions on governance.",
        "image": "./assets/jobs/politician.png"
    },
    "social_worker": {
        "title": "Social Worker 🤝",
        "description": "Social workers assist individuals and communities in overcoming challenges and improving well-being.",
        "image": "./assets/jobs/social_worker.png"
    },
    "receptionist": {
        "title": "Receptionist ☎️",
        "description": "Receptionists manage front-desk operations, greeting visitors and handling administrative tasks.",
        "image": "./assets/jobs/receptionist.png"
    },
    "sales_representative": {
        "title": "Sales Representative 🛍️",
        "description": "Sales representatives promote and sell products or services, building client relationships.",
        "image": "./assets/jobs/sales_representative.png"
    },
    "counselor": {
        "title": "Counselor 🧠",
        "description": "Counselors provide guidance and support to individuals facing personal or psychological challenges.",
        "image": "./assets/jobs/counselor.png"
    },
    "athlete": {
        "title": "Athlete 🏅",
        "description": "Athletes compete in sports, demonstrating physical prowess and dedication.",
        "image": "./assets/jobs/athlete.png"
    },
    "dancer": {
        "title": "Dancer 💃",
        "description": "Dancers express ideas and emotions through movement, performing in various settings.",
        "image": "./assets/jobs/dancer.png"
    },
    "Mechanic": {
        "title": "Mechanic 🔧",
        "description": "Mechanics inspect and repair vehicles and machinery, ensuring optimal performance.",
        "image": "./assets/images/mechanic.png"
    },
    "actor_actress": {
        "title": "Actor/Actress 🎭",
        "description": "Actors and actresses portray characters in performances, bringing stories to life.",
        "image": "./assets/jobs/actor_actress.png"
    },
    "physical_therapist": {
        "title": "Physical Therapist 🏃",
        "description": "Physical therapists help patients recover mobility and manage pain through therapeutic exercises.",
        "image": "./assets/jobs/physical_therapist.png"
    },
    "editor": {
        "title": "Editor ✍️",
        "description": "Editors review and revise content for clarity, accuracy, and coherence.",
        "image": "./assets/jobs/editor.png"
    },
    "historian": {
        "title": "Historian 📜",
        "description": "Historians research and interpret past events, contributing to our understanding of history.",
        "image": "./assets/jobs/historian.png"
    },
    "journalist": {
        "title": "Journalist 📰",
        "description": "Journalists investigate and report on news and events, informing the public.",
        "image": "./assets/jobs/journalist.png"
    },
    "language_teacher": {
        "title": "Language Teacher 🗣️",
        "description": "Language teachers instruct students in foreign languages, enhancing communication skills.",
        "image": "./assets/jobs/language_teacher.png"
    },
    "poet": {
        "title": "Poet ✒️",
        "description": "Poets craft expressive works using rhythm and language to convey emotions and ideas.",
        "image": "./assets/jobs/poet.png"
    },
    "broadcaster": {
        "title": "Broadcaster 📻",
        "description": "Broadcasters present news and entertainment content via television, radio, or online platforms.",
        "image": "./assets/jobs/broadcaster.png"
    },
    "artist": {
        "title": "Artist 🎨",
        "description": "Artists create visual works to express ideas, emotions, or concepts.",
        "image": "./assets/jobs/artist.png"
    },
    "graphic_designer": {
        "title": "Graphic Designer 🖌️",
        "description": "Graphic designers develop visual content to communicate messages effectively.",
        "image": "./assets/jobs/graphic_designer.png"
    },
    "fashion_designer": {
        "title": "Fashion Designer 👗",
        "description": "Fashion designers create clothing and accessories, blending aesthetics with functionality.",
        "image": "./assets/jobs/fashion_designer.png"
    },
    "interior_decorator": {
        "title": "Interior Decorator 🛋️",
        "description": "Interior decorators enhance spaces by selecting furnishings, color schemes, and layouts to create aesthetic and functional environments.",
        "image": "./assets/jobs/interior_decorator.png"
    },
    "Pilot": {
        "title": "Pilot ✈️",
        "description": "Pilots navigate the skies, transporting people and goods safely around the world.",
        "image": "./assets/jobs/pilot.png"
    },
    "Psychologist": {
        "title": "Psychologist 🧠",
        "description": "Psychologists study human behavior and help individuals improve their mental well-being.",
        "image": "./assets/jobs/psychologist.png"
    },
    "Philosopher": {
        "title": "Philosopher 🧘",
        "description": "Philosophers explore life's biggest questions through critical thinking and deep reflection.",
        "image": "./assets/jobs/philosopher.png"
    },
    "Writer": {
        "title": "Writer ✍️",
        "description": "Writers express ideas, tell stories, and share knowledge through the power of words.",
        "image": "./assets/jobs/writer.png"
    },
    "Criminologist": {
        "title": "Criminologist 🕵️",
        "description": "Criminologists analyze crime patterns and work on solutions to improve justice systems.",
        "image": "./assets/jobs/criminologist.png"
    },
    "Company secretary": {
        "title": "Company Secretary 🗂️",
        "description": "Company Secretaries ensure businesses comply with regulations and maintain corporate governance.",
        "image": "./assets/jobs/company_secretary.png"
    },
    "Marketing": {
        "title": "Marketing Specialist 📣",
        "description": "Marketing professionals promote products and connect brands with customers.",
        "image": "./assets/jobs/marketing.png"
    },
    "Logistics manager": {
        "title": "Logistics Manager 🚚",
        "description": "Logistics Managers coordinate supply chains and ensure timely delivery of goods.",
        "image": "./assets/jobs/logistics_manager.png"
    },
    "Research analyst": {
        "title": "Research Analyst 🔬",
        "description": "Research Analysts collect and interpret data to help businesses make informed decisions.",
        "image": "./assets/jobs/research_analyst.png"
    },
    "Business manager": {
        "title": "Business Manager 💼",
        "description": "Business Managers oversee operations and lead teams to meet organizational goals.",
        "image": "./assets/jobs/business_manager.png"
    },
    "Internal auditor": {
        "title": "Internal Auditor 📊",
        "description": "Internal Auditors assess financial records to ensure accuracy and compliance.",
        "image": "./assets/jobs/internal_auditor.png"
    },
    "Chief financial officer": {
        "title": "Chief Financial Officer (CFO) 💹",
        "description": "CFOs manage the financial health of organizations and guide strategic planning.",
        "image": "./assets/jobs/cfo.png"
    },
    "Business Analyst": {
        "title": "Business Analyst 📈",
        "description": "Business Analysts bridge the gap between IT and business, driving growth with data insights.",
        "image": "./assets/jobs/business_analyst.png"
    },
    "Banking": {
        "title": "Banker 🏦",
        "description": "Bankers manage financial transactions, advise clients, and support economic growth.",
        "image": "./assets/jobs/banker.png"
    },
    "Stock Broker": {
        "title": "Stock Broker 📉📈",
        "description": "Stock Brokers trade securities and guide investors through financial markets.",
        "image": "./assets/jobs/stock_broker.png"
    },
    "Financial Advisor": {
        "title": "Financial Advisor 💰",
        "description": "Financial Advisors help individuals plan and manage their finances wisely.",
        "image": "./assets/jobs/financial_advisor.png"
    },
    "Consultant": {
        "title": "Consultant 📋",
        "description": "Consultants offer expert advice to solve problems and improve organizational performance.",
        "image": "./assets/jobs/consultant.png"
    },
    "Archeologist": {
        "title": "Archaeologist 🏺",
        "description": "Archaeologists study ancient cultures by excavating and analyzing artifacts.",
        "image": "./assets/jobs/archaeologist.png"
    },
    "Pre Primary Teacher (2020 NEP and Mental Health)": {
        "title": "Pre-Primary Teacher 🎨",
        "description": "Pre-primary teachers nurture young minds, laying the foundation for lifelong learning.",
        "image": "./assets/jobs/pre_primary_teacher.png"
    },
    "Primary Teacher": {
        "title": "Primary School Teacher ✏️",
        "description": "Primary teachers educate children in their early, most formative years.",
        "image": "./assets/jobs/primary_teacher.png"
    },
    "Middle": {
        "title": "Middle School Teacher 📘",
        "description": "Middle school teachers guide students through academic and personal growth.",
        "image": "./assets/jobs/middle_school_teacher.png"
    },
    "Higher School Teacher and Professors": {
        "title": "High School Teacher / Professor 🎓",
        "description": "Teachers and professors in higher education inspire the next generation of leaders and thinkers.",
        "image": "./assets/jobs/higher_teacher.png"
    },
    "Anthropologist": {
        "title": "Anthropologist 🌍",
        "description": "Anthropologists study human societies, cultures, and their development across time.",
        "image": "./assets/jobs/anthropologist.png"
    },
    "Medical": {
        "title": "Medical Professional 🏥",
        "description": "Medical professionals diagnose and treat health conditions to improve lives.",
        "image": "./assets/jobs/medical.png"
    },
    "Para Medical": {
        "title": "Paramedical Staff 🩺",
        "description": "Paramedical workers support medical teams through therapy, nursing, and diagnostics.",
        "image": "./assets/jobs/paramedical.png"
    },
    "Militry": {
        "title": "Military Personnel 🎖️",
        "description": "Military personnel serve and protect the nation, demonstrating courage and discipline.",
        "image": "./assets/jobs/military.png"
    },
    "Para Militry": {
        "title": "Paramilitary Forces 🔰",
        "description": "Paramilitary forces provide internal security and support during emergencies.",
        "image": "./assets/jobs/paramilitary.png"
    },
    "Police Force": {
        "title": "Police & Intelligence Forces 🕵️‍♀️",
        "description": "Police and intelligence officers uphold law and order and investigate criminal activity.",
        "image": "./assets/jobs/police.png"
    },
    "Technician": {
        "title": "Technician 🔧",
        "description": "Technicians operate, maintain, and repair equipment across various industries.",
        "image": "./assets/jobs/technician.png"
    }
}

    
# ---------- Get Prediction from Session ----------
if "prediction" not in st.session_state:
    st.error("No prediction found. Please take the test first.")
    st.stop()

job_key = st.session_state["prediction"][0]
job = job_data.get(job_key) 

# ---------- Display Job Info ----------
if job:
    # Title - centered
    st.markdown(f"<h1 style='color:#b03a64; text-align: center;'>{job['title']}</h1>", unsafe_allow_html=True)
    
    
    col1, col2 = st.columns(2)  # Create three columns again for centering the button
    with col1:
        st.subheader("🚗 Road to Becoming a Mechanic in Morocco")
        # Description and back link - centered
        st.markdown(f"""
            <div class="career-description" style="font-size: 1.1em; color: #5e4b56; text-align: center; max-width: 700px; margin: 20px auto;">
                {job['description']}
            </div>
            <br>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("🔗 External Resources to Explore")

        st.markdown('<a class="section" href="https://www.ofppt.ma" target="_blank">OFPPT Official Website</a>', unsafe_allow_html=True)
        st.markdown('<a class="resource-link" href="https://www.orientations.ma/" target="_blank">Orientations.ma - Career Guidance</a>', unsafe_allow_html=True)
        st.markdown('<a class="resource-link" href="https://www.skills.ma" target="_blank">Skills.ma - Vocational Training Opportunities</a>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)


    # # Centering the image with st.image
    # col1, col2, col3 = st.columns([1, 2, 1])  # Create three columns to center the image
    # with col2:
    #     st.image(job["image"], width=300)



    # Centering the back button
    col1, col2, col3 = st.columns([1, 2, 1])  # Create three columns again for centering the button
    with col2:
        st.markdown("""
            <a href="/" class="back-button" style="text-decoration: none; font-weight: bold; color: #b03a64; text-align: center;">← Back to Home</a>
        """, unsafe_allow_html=True)
    










