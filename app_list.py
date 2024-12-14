import streamlit as st

st.title("Apps with endless possibilities")
st.write("""The advancement of technology was intended to reduce officers' workload; however, evidence shows that officers remain overloaded with administrative tasks 
            despite police departments' investments in modernization of various systems.
            Machine learning and AI offer a promissing solution. These proof of concept apps demostrate the application of machine learning, from basic model to advanced AI model to assist with various tasks.
            The main purpose of these concepts is to promote awareness and to help officers manage the significant increase in adminstrative and investigative tasks in the past decade.""")

st.markdown("<p><h3><span style='color: blue;'>Offence Classifier</h3></span></p>", unsafe_allow_html=True)
st.write("This is a basic machine learning model using Logistic Regression with TF-IDF vectorizer to classify offences. The model was train on only 40 examples. The larger the training dataset, the higher the accuracy. This model works locally and does not require connection to the internet.")
st.markdown("[<h3>Try it</h3>](https://my-qc-app-7ij5uuv4vgp3nhyzrhttdm.streamlit.app/)", unsafe_allow_html=True)
st.write("")

st.markdown("<p><h3><span style='color: blue;'>Similarity Search</h3></span></p>", unsafe_allow_html=True)
st.write("""This exercise demostrates the application of using Cosine Similarity from a pre-trained LLM model, specifically paraphrase-MiniLM-L6-v2 to identify similar texts. 
            The concept can be used to find similar MOs in the database and can be useful in detecting patterns in criminal activities. This model works locally and does not require connection to the internet.""")
st.markdown("[<h3>Try it</h3>](https://cs-transformer.streamlit.app/)", unsafe_allow_html=True)
st.write("")

st.markdown("<p><h3><span style='color: blue;'>Name Entity Recogition</h3></span></p>", unsafe_allow_html=True)
st.write("""This demo shows the posiblity to using a pre-trained NER AI model to identify entities such as name, location, and mamy others within a text page. With this
            in mind, the possibilities are up to what you want to achive! This model works locally and does not require connection to the internet. """)
st.markdown("[<h3>Try it</h3>](https://ner-police.streamlit.app/)", unsafe_allow_html=True)
st.write("")

st.markdown("<p><h3><span style='color: blue;'>eIM</h3></span></p>", unsafe_allow_html=True)
st.write("""This proof of concept uses the most advanced AI model to generate an eIM compliant RTCC or any report with
            all entities and text pages in an XML file. The file can be imported for further processing or sent directly to
            the Transcription Queue for further processing. This model uses the free version of Gemini and all data is sent to the server for processing; therefore confidential information is not recommended.""")
st.markdown("[<h3>Try it</h3>](https://eim-api.streamlit.app/)", unsafe_allow_html=True)
st.write("")
st.markdown("**Although these demos show that these models work independently, it is possible to combine them for achieving certain goal. For example, NER can be used to remove confidential information prior to sending the text to the AI model for further processing.**")



         
