import mysql.connector
from openai import OpenAI


def connect_db():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3308,
        user='root',
        password='',
        database='Data_Nest'
    )
    return conn


client = OpenAI(api_key='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')


