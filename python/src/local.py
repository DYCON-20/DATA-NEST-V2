import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3308,
        user='root',
        password='',
        database='Data_Nest'
    )
    return conn
