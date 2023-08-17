import streamlit as st

st.header("Contact Me")

with st.form(key='email_forms'):
    user_email = st.text_input("Your Email address")
    message = st.text_area("Your Message")
    button = st.form_submit_button("Submit")

    if button:
        # if button is presseed send an email
        message = message + user_email
        