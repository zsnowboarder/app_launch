import streamlit as st

st.title("Apps")
st.write("These proof of concept apps demostrate the application of machine learning, from basic model to advanced AI model to assist with various tasks.")

st.markdown("<p><h3><span style='color: blue;'>Offence Classifier</h3></span></p>", unsafe_allow_html=True)
st.write("This is a basic machine learning model using Logistic Regression to classify offences. The mode was train on less than 100 examples.")
st.markdown("[<h3>Try it</h3>](https://my-qc-app-7ij5uuv4vgp3nhyzrhttdm.streamlit.app/)", unsafe_allow_html=True)
st.write("")

st.markdown("<p><h3><span style='color: blue;'>Similarity Search</h3></span></p>", unsafe_allow_html=True)
st.write("""This exercise demostrates the application of using Cosine Similarity from a pre-trained LLM model, specifically paraphrase-MiniLM-L6-v2 to identify similar texts. 
            The concept can be used to find similar MOs in the database and can be useful in detecting patterns in criminal activities.""")
st.markdown("[<h3>Try it</h3>](https://cs-transformer.streamlit.app/)", unsafe_allow_html=True)
st.write("")

st.markdown("<p><h3><span style='color: blue;'>eIM</h3></span></p>", unsafe_allow_html=True)
st.write("""This proof of concept uses the most advanced AI model to generate an eIM compliant RTCC or any report with
            all entities and text pages in an XML file. The file can be imported for further processing or sent directly to
            the Transcription Queue for further processing.""")
st.markdown("[<h3>Try it</h3>](https://eim-api.streamlit.app/)", unsafe_allow_html=True)
st.write("")

         
