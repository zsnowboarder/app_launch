import streamlit as st
#import getpass, pytz, os
import pytz
from datetime import datetime

timezone = pytz.timezone("America/Los_Angeles")

def get_greeting():
    now = datetime.now(timezone)
    if now.hour < 12:
        return "Good morning"
    elif 12 <= now.hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


greeting = get_greeting()
#username = getpass.getuser()
#username = os.getenv('USERNAME') or os.getenv('USER')
st.title(greeting)
st.title("🤖 Apps with endless possibilities")
st.write("""one of the main purposes of advancement of technology should be to increase productivity and reduce officers' workload; 
            however, evidence has shown that officers remain overloaded with administrative tasks 
            despite police departments' investments in modernization of various systems. Police departments are often lagged behind in rapidly developing applications and tools
            using free cutting edge technology such as machine learning and AI to solve problems. 
            These proof of concept apps demostrate the application of machine learning, from basic model to advanced AI model to assist with various tasks.
            The main purpose of these concepts is to promote awareness and to help officers and civilian employees manage the increasing demand in adminstrative and investigative tasks in modern policing enviroment.""")

st.markdown("<p><h3><span style='color: blue;'>1.📑 Offence Classifier</h3></span></p>", unsafe_allow_html=True)
st.write("This is a basic machine learning model using Logistic Regression with TF-IDF vectorizer to classify offences. The model was train on only 40 examples. The larger the training dataset, the higher the accuracy. This model works locally and does not require connection to the internet.")
st.markdown("[<h3>Try it</h3>](https://my-qc-app-7ij5uuv4vgp3nhyzrhttdm.streamlit.app/)", unsafe_allow_html=True)
st.write("")

st.markdown("<p><h3><span style='color: blue;'>2.🔍 Similarity Search</h3></span></p>", unsafe_allow_html=True)
st.write("""This exercise demostrates the application of using Cosine Similarity from a pre-trained LLM model, specifically paraphrase-MiniLM-L6-v2 to identify similar texts. 
            The concept can be used to find similar MOs in the database and can be useful in detecting patterns in criminal activities. This model works locally and does not require connection to the internet.""")
st.markdown("[<h3>Try it</h3>](https://cs-transformer.streamlit.app/)", unsafe_allow_html=True)
st.write("")

st.markdown("<p><h3><span style='color: blue;'>3.🏷️ Name Entity Recogition</h3></span></p>", unsafe_allow_html=True)
st.write("""This demo shows the posiblity to using a pre-trained NER AI model to identify entities such as name, location, and mamy others within a text page. With this
            in mind, the possibilities are up to what you want to achive! This model works locally and does not require connection to the internet. """)
st.markdown("[<h3>Try it</h3>](https://ner-police.streamlit.app/)", unsafe_allow_html=True)
st.write("")

st.markdown("<p><h3><span style='color: blue;'>4.🔄️ Supervised and Unsupervised ML</h3></span></p>", unsafe_allow_html=True)
st.write("""This demostrates using a combinating of supervised and unsupervised machine learning to solve a threat analysis problem. In this case, identifying unusual or a change in behaviour.
This model works locally and does not require connection to the internet.""")
st.markdown("[<h3>Try it</h3>](https://threat-analysis.streamlit.app/)", unsafe_allow_html=True)
st.write("")

st.markdown("<p><h3><span style='color: blue;'>5.✨ eIM</h3></span></p>", unsafe_allow_html=True)
st.write("""This proof of concept uses the most advanced AI model to generate an eIM compliant RTCC or any report with
            all entities and text pages in an XML file. The file can be imported for further processing or sent directly to
            the Transcription Queue for further processing. This model uses the free version of Gemini and all data is sent to the server for processing; therefore confidential information is not recommended.""")
st.markdown("[<h3>Try it</h3>](https://eim-api.streamlit.app/)", unsafe_allow_html=True)
st.write("")

st.markdown("<p><h3><span style='color: blue;'>6.🔍 Threat and Sentiment Detection</h3></span></p>", unsafe_allow_html=True)
st.write("""This demo retrieves the latest 10 news articles from CTV News and analyses the content. User will have an opportunity to add an additional text for analysis. This concept can be used to monitor threats for 
specific user's social media account using an API.""")
st.markdown("[<h3>Try it</h3>](https://threat-detoxify.streamlit.app/)", unsafe_allow_html=True)
st.write("")

st.markdown("""**These concepts have demostrated the application of ML and AI to solve problems and to help generate more ideas as well as curiosities.
Although these demos show that these models work independently, it is possible to combine them to navigate hrough a workflow with higher complexity. 
For example, NER can be used to remove confidential information prior to sending the text to the AI model for further processing.
In addition, further work can be done to leverage these models for real time threat or emergent trend monitoring using unsupervise learning to identify themes.
The possibilities are endless.**""")


ai = """[The following is AI generated content] AI is a powerful tool that, when combined with machine learning, can perform 
exceptionally well for a wide range of tasks, ultimately enhancing human capabilities and driving progress. By automating routine tasks, AI allows 
humans to focus on more complex and creative aspects of their work, leading to increased productivity and innovation. The collaboration between human 
intelligence and AI's computational power opens up new horizons for solving complex problems and generating innovative ideas.
These advancements spark curiosity and open up new possibilities for various sectors, including police agencies, healthcare, finance, and more. 
For police agencies, in particular, the integration of AI and ML can revolutionize investigative processes, enhance threat detection, and improve 
overall efficiency. By embracing these technologies, police agencies can better manage administrative tasks, identify patterns in criminal activities, 
and respond more effectively to emerging threats."""
