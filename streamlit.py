import streamlit as st
import spacy
from spacy import displacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to check username and password
def check_auth(username, password):
    return username == "admin" and password == "password"

# Streamlit app
st.title("Entity Recognition with spaCy")

# Session state to keep track of authentication
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Authentication form
if not st.session_state.authenticated:
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if check_auth(username, password):
            st.session_state.authenticated = True
            st.success("Authenticated successfully!")
        else:
            st.error("Invalid username or password")
else:
    # Text input
    text = st.text_area("Enter text to analyze:")
    if st.button("Analyze"):
        if text:
            doc = nlp(text)
            # Render the entities using displacy
            html = displacy.render(doc, style="ent")
            # Display the rendered HTML
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.write("Please enter some text to analyze.")

    # Logout button
    if st.button("Logout"):
        st.session_state.authenticated = False