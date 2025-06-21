import mysql.connector as ms
import pandas as pd

def get_connection(db_name):

    conn = ms.connect(
        host="localhost",     
        user="root",          
        password="vini", 
        database=db_name
    )

    cursor = conn.cursor()

    return cursor


def sql_to_df(table_name,_cursor):
    
    _cursor.execute(f"SELECT * FROM {table_name}")
    result = _cursor.fetchall()

    df = pd.DataFrame(result)
    
    return df



def load_data(cursor):
    
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    dataframes = {}
    for i in tables:
        table_name = i[0]
        dataframes[table_name] = sql_to_df(table_name,cursor)

    return dataframes








    













