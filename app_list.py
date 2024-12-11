import streamlit as st

st.title("Apps")
st.write("These proof of concept apps demostrate the application of machine learning, from basic model to advanced AI model to assist with various tasks.")

st.markdown("<p><h3><span style='color: blue;'>Offence Classifier</h3></span></p>", unsafe_allow_html=True)
st.write("""This machine learning model uses Logistic Regression with TF-IDF vectorizer to classify offenses. 
            It was trained on fewer than 100 examples, and a larger dataset will improve accuracy. This model works locally and does not require connection to the internet. """)
st.markdown("[<h3>Try it</h3>](https://my-qc-app-7ij5uuv4vgp3nhyzrhttdm.streamlit.app/)", unsafe_allow_html=True)
st.write("")

st.markdown("<p><h3><span style='color: blue;'>Similarity Search</h3></span></p>", unsafe_allow_html=True)
st.write("""This exercise demonstrates the application of Cosine Similarity using a pre-trained LLM model, specifically paraphrase-MiniLM-L6-v2, to identify similar texts. 
            LLM models like this are designed to capture meanings and the context of the texts to a certain extend, making it useful to find similar MOs in a database and detect patterns in criminal activities. 
            This model works locally and does not require connection to the internet. """)
st.markdown("[<h3>Try it</h3>](https://cs-transformer.streamlit.app/)", unsafe_allow_html=True)
st.write("")

st.markdown("<p><h3><span style='color: blue;'>eIM</h3></span></p>", unsafe_allow_html=True)
st.write("""This proof of concept leverages an advanced AI model to generate an eIM compliant RTCC or any report with all entities and text pages in an XML file. 
            The generated file can be imported for further processing or sent directly to the Transcription Queue for processing.  This model uses the free version of Gemini and all data is sent to the server for processing; 
            therefore confidential information is not recommended. """)
st.markdown("[<h3>Try it</h3>](https://eim-api.streamlit.app/)", unsafe_allow_html=True)
st.write("")

         
