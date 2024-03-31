from Setting.setting import  connect_db
from datetime import datetime, timedelta

def Source():
    conn = connect_db()
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS Sources (
        ID SERIAL PRIMARY KEY,
        Date DATE NOT NULL,
        Content TEXT NOT NULL
    )
    """
    cursor.execute(create_table_query)

    conn.commit()

    yesterday_date = datetime.now() - timedelta(1)
    yesterday_str = yesterday_date.strftime('%Y-%m-%d')

    cursor.execute("SELECT * FROM Sources WHERE Date = %s", (yesterday_str,))
    if cursor.fetchone() is None:

        cursor.execute("SELECT User, Texte FROM Article_Thread WHERE Date_Thread LIKE %s", (yesterday_str + '%',))
        yesterday_date_threads_resultat = cursor.fetchall()

        source_content = "IT monitoring from " + yesterday_str + " Thread = " + str(yesterday_date_threads_resultat)
        insert_query = "INSERT INTO Sources (Date, Content) VALUES (%s, %s)"
        cursor.execute(insert_query, (yesterday_str, source_content))

        conn.commit()
    else:
        print("Une entrée existe déjà pour la date", yesterday_str)

    conn.close()

