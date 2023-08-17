import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key='email_forms'):
    user_email = st.text_input("Your Email address")
    message = st.text_area("Your Message")
    message = message + "\n" + user_email
    button = st.form_submit_button("Submit")

    if button:
        # if button is presseed send an email
        send_email(message)
