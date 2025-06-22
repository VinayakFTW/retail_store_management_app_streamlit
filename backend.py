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



def load_data():
    conn = get_connection("retail_store")
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    dataframes = {}
    for i in tables:
        table_name = i[0]
        dataframes[table_name] = sql_to_df(table_name)

    return dataframes


def add_categories(cursor,cat_name):

    return 





    













