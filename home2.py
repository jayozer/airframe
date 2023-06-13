

import streamlit as st
import os

st.set_page_config(layout="centered", page_title="Airframe Login", page_icon="👩🏻‍💻")

image = "images/icon_one.png"
st.image(image, width=100)

# st.title(f"My Title<img src='{image}' width='100' align='center'>".format(image))
st.title(':orange[Airframe-Stream: ] Ingest data into Snowflake ')

# Define accepted user name and password combinations
users = {
    "jay.ozer@doma.com": "admin",
    "test.test@doma.com": "admin"
}

# Define authorization page
def login():
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if email in users:
            if password == users[email]:
                st.success("Logged in as {}. \n\n Select a category from the sidebar to begin editing.".format(email))
                return True
            else:
                st.error("Incorrect email or password")
        else:
            st.error("Incorrect email or password")
    return False

# Define main function
def main(): 
    st.sidebar.title("Categories")
    app_mode = st.sidebar.selectbox("Choose the app mode",
        ["Show instructions", "Show the source code"])
    if app_mode == "Show instructions":
        st.sidebar.success('To continue select "Run the app".')
    elif app_mode == "Show the source code":
        st.code(__file__)
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app is a demo of Airframe-Stream.
        """
    )
   

# Run the app
if login():
    main()

