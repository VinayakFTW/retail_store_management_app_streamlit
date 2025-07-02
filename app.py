import streamlit as st
import pandas as pd
from backend import *

st.set_page_config(page_title="Home", page_icon="🏠")

    
if "auth" not in st.session_state:
        st.session_state.auth = False

if "add_prod" not in st.session_state:
        st.session_state.add_prod = False

if "cat_id" not in st.session_state:
        st.session_state.cat_id = None


if not(st.session_state.auth):
    st.title("Enter your credentials")
    if "show_create_form" not in st.session_state:
        st.session_state.show_create_form = False
    if "show_login_form" not in st.session_state:
        st.session_state.show_login_form = False

    if st.button("Login",key="login_form"):
        st.session_state.show_login_form = True
        st.session_state.show_create_form = False
            
    if st.session_state.show_login_form:
        st.title("Login")
        with st.form("login_form"):
            username = st.text_input("Username")
            st.session_state.username = username
            password = st.text_input("Password", type="password")
            submit_button = st.form_submit_button("Login")
            if submit_button:
                if authenticate_user(username, password):
                    st.session_state.auth = True
                    st.session_state.show_login_form = False
                    st.success("Successfully Logged in")
                    st.rerun()
                else:
                    st.error("Username or password incorrect")

    if st.button("Create New Account"):
        st.session_state.show_login_form = False
        st.session_state.show_create_form = True    
    
    if st.session_state.show_create_form:
        st.title("Create New Account")
        with st.form("create_form"):
            new_usr =st.text_input("Username")
            new_pswd = st.text_input("Password",type="password")
            new_email = st.text_input("Email")
            submit_button = st.form_submit_button("Create Account",)
            if submit_button:
                if create_user(new_usr,new_pswd,new_email):
                    st.session_state.auth = True
                    st.session_state.show_create_form = False
                    st.success("Successfully Created Account")
                    st.rerun()
                else:
                    st.error("ERR-01-account with email already exists")

if st.session_state.auth:
    
    title_placeholder = st.empty()

    if st.session_state.add_prod:
        title_placeholder.title("Add Product")
        with st.form("add_prod_form"):    
            p_nm = st.text_input("Product Name")
            desc = st.text_input("Description")
            cat_id = st.number_input("Category Id")
            stock_qty = st.number_input("Stock Quantity")
            price = st.number_input("Price")
            sup_id = st.number_input("Supplier Id")
            

            submit_button = st.form_submit_button("Add Product")

            if submit_button:
                create_product(p_nm,desc,price,stock_qty,cat_id,sup_id)
                st.success("Successfully Added Product")
                st.session_state.add_prod = False
                st.rerun()
    
    title_placeholder.title(f"🏠Welcome {st.session_state.username}")
    df = load_all_data()
    categories = df["categories"]
    cat_names = st.radio("Select Category",[cat for cat in categories.category_name])
    cat_id_dict = {}
    for i,cat in zip(categories.category_id,categories.category_name):
        cat_id_dict[cat] = i
    cat_id = cat_id_dict[cat_names]

    products = df["products"]
    products = products[products.category_id == cat_id]
    product_names = products.product_name
    st.dataframe(products)


    if st.button("Add Product"):
        st.session_state.cat_name = cat_names
        st.session_state.add_prod = True
        st.rerun()



