import psycopg2
from datetime import datetime

def create_db_connection():
    conn = psycopg2.connect(host='', 
    port=5432, 
    user='', 
    password='',
    database='', 
    sslmode='require')
    return conn

def post_search_data(user_id, keyword):
    connection = create_db_connection()
    sql_cursor = connection.cursor()
    sql_cursor.execute("Insert into public.searches Values('{}', '{}', '{}')".format(
        user_id, keyword, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    connection.commit()
    connection.close()

def fetch_search_data(user_id, keyword):
    connection = create_db_connection()
    sql_cursor = connection.cursor()
    sql_cursor.execute("Select * from public.searches where user_id = '{}' and keyword like '%".format(user_id) + keyword +"%'")
    results = sql_cursor.fetchall()
    connection.close()
    return results
    