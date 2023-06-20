import streamlit as st
import os
from ldap3 import Server, Connection

st.set_page_config(layout="centered", page_title="Airframe Login", page_icon="👩🏻‍💻")

image = "images/icon_one.png"
st.image(image, width=100)

st.title(':orange[Airframe-Stream: ] Ingest data into Snowflake ')

# Define your Active Directory server information
AD_SERVER = 'your_ad_server'
AD_PORT = 389
AD_USER = 'your_ad_user'
AD_PASS = 'your_ad_password'

# Define authorization page
def login():
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        server = Server(AD_SERVER, port=AD_PORT, get_info="ALL")
        conn = Connection(server, user=AD_USER, password=AD_PASS, auto_bind=True)
        conn.search('dc=doma,dc=com', f'(&(objectClass=person)(mail={email})(userPassword={password}))')
        if conn.entries:
            st.success("Logged in as {}. \n Select a category from the sidebar to begin editing.".format(email))
            return True
        else:
            st.error("Incorrect email or password")
        
    return False

# Define sidebar
def sidebar():
    ...
    
# Define main function
def main():
    sidebar()

# Run the app
if login():
    main()
