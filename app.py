import streamlit as st
import pandas as pd
from backend import *

st.set_page_config(page_title="Home", page_icon="🏠")


# Dropdown menu
menu = ["Home", "Products"]
choice = st.sidebar.selectbox("Menu", menu)
auth = False
if "show_create_form" not in st.session_state:
    st.session_state.show_create_form = False
if "show_login_form" not in st.session_state:
    st.session_state.show_login_form = False
if choice == "Home":
    st.title("🏠 Home")
    if st.button("Login",key="login_form"):
        st.session_state.show_login_form = True
        
    if st.session_state.show_login_form:
        usr =st.text_input("Username",key="login_username")
        pswd = st.text_input("Password",key="login_password")
        if st.button("Login",key="login_button"):
            if authenticate_user(usr,pswd):
                auth = True
                st.success("Successfully Logged in")
            else:
                st.error("Username or password incorrect")

    if st.button("Create New Account"):
        st.session_state.show_create_form = True
   
    if st.session_state.show_create_form:
        new_usr =st.text_input("Username",key="create_username")
        new_pswd = st.text_input("Password",key="create_password",type="password")
        new_email = st.text_input("Email",key="create_email")
        if st.button("Create Account"):
            if create_user(new_usr,new_pswd,new_email):
                st.success("Successfully Created Account")
            else:
                st.error("ERR-01-account with email or phone number already exists")


elif choice == "Products":
    st.title("Products")





