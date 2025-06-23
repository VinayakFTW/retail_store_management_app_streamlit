import mysql.connector as ms
import pandas as pd

def get_connection(db_name):

    conn = ms.connect(
        host="localhost",     
        user="root",          
        password="vini", 
        database=db_name
    )


    return conn


def sql_to_df(table_name):
    conn = get_connection("retail_store")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    result = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(result)
    df.columns = columns
    
    return df



def load_all_data():
    conn = get_connection("retail_store")
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    dataframes = {}
    for i in tables:
        table_name = i[0]
        dataframes[table_name] = sql_to_df(table_name)

    return dataframes

def get_all_products():
    conn = get_connection("retail_store")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    result = cursor.fetchall()
    columns = cursor.column_names
    products = pd.DataFrame(result)
    products.columns = columns
    
    return products

def update_product(product_id, name, category, price, quantity):
    conn = get_connection("retail_store")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE products SET name={name}, category={category}, price={price}, quantity={quantity} WHERE id={product_id}")
    conn.commit()


def create_product(name, category, price, quantity):
    conn = get_connection("retail_store")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO products (name, category, price, quantity) VALUES ({name}, {category}, {price}, {quantity})")
    conn.commit()

def delete_product(product_id):
    conn = get_connection("retail_store")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=%s", (product_id,))
    conn.commit()

def authenticate_user(username, password):
    conn = get_connection("retail_store")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False

def create_user(username,password,email):
    conn = get_connection("retail_store")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username,password,email) VALUES (%s,%s,%s)",(username,password,email))
    conn.commit()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    verify = cursor.fetchone()
    if verify:
        return True
    else:
        return False

    













