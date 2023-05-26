

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

# Define sidebar
def sidebar():
    st.sidebar.title("Airframe Data Editor")
    st.sidebar.header("Bases")
    
    base1 = st.sidebar.radio("TE_TIME_Employee", ["TE_TIME_Employee_Map", "Frame 2"])
    if base1 == "TE_TIME_Employee_Map":
        st.write("TE_TIME_Employee_Map")
    else:
        st.write("Frame 2")

    base2 = st.sidebar.radio("EDM_Metadata", ["Order_Project_Channel_Map", "Order_Status_Group_Lkp"])
    if base2 == "Order_Project_Channel_Map":
        st.write("Order_Project_Channel_Map")
    else:
        st.write("Order_Status_Group_Lkp")
    
    base3 = st.sidebar.radio("TE_TIME_Process_Point", ["Agency_External_Users", "TE_Time_Action_Weight_Lkp"])
    if base3 == "Agency_External_Users":
        st.write("Agency_External_Users")
    else:
        st.write("TE_Time_Action_Weight_Lkp")


# Define main function
def main():
    sidebar()

# Run the app
if login():
    main()

