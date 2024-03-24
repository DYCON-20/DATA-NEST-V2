import mysql.connector
from mysql.connector import Error
from Setting.setting import  connect_db_creat

def setting_bdd():
        
    conn = connect_db_creat()
    cursor = conn.cursor()
    try:
        conn = connect_db_creat()


        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS Data_Nest")
            cursor.execute("USE Data_Nest")

            # Créer les tables
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Video_mots (
                    id INT(11) AUTO_INCREMENT PRIMARY KEY,
                    date VARCHAR(10),
                    mots_clee_1 TEXT,
                    mots_clee_2 TEXT,
                    mots_clee_3 TEXT,
                    mots_clee_4 TEXT,
                    mots_clee_5 TEXT
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Article_Thread (
                    id INT(11) AUTO_INCREMENT PRIMARY KEY,
                    id_Thread VARCHAR(500),
                    User VARCHAR(500),
                    Texte VARCHAR(500),
                    Lien_images VARCHAR(500),
                    Lien_video VARCHAR(500),
                    Date_Thread VARCHAR(500)
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Video_filtre (
                    id INT(11) AUTO_INCREMENT PRIMARY KEY,
                    date VARCHAR(10),
                    Video_filtre1 TEXT,
                    Video_filtre2 TEXT,
                    Video_filtre3 TEXT,
                    Video_filtre4 TEXT,
                    Video_filtre5 TEXT
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Video_script (
                    id INT(11) AUTO_INCREMENT PRIMARY KEY,
                    date VARCHAR(10),
                    script_article_1 TEXT,
                    script_article_2 TEXT,
                    script_article_3 TEXT,
                    script_article_4 TEXT,
                    script_article_5 TEXT
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Article_Filtre (
                    id INT(11) AUTO_INCREMENT PRIMARY KEY,
                    Filtre_resultat TEXT,
                    date VARCHAR(10)
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Article_final (
                    id INT(11) AUTO_INCREMENT PRIMARY KEY,
                    Article_resultat TEXT,
                    date VARCHAR(10)
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Sources (
                    ID BIGINT(20) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                    Date DATE,
                    Content TEXT
                )
            """)

            print("Les tables ont été créées avec succès.")
    except Error as e:
        print("Erreur lors de la connexion à MySQL:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("La connexion MySQL est fermée.")
