import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import mysql.connector
from datetime import datetime
from urllib.parse import quote
from setting import connect_db
def recuperationbdd(donnees_a_inserer):

    try:
        conn = connect_db()

   
        if conn.is_connected():
            print("­­­­­–")
            print("1️⃣〔MySQL database connection established. 〕1️⃣")

        # Création d'un curseur
        # Creating a cursor
        cur = conn.cursor()

        # Commande SQL pour créer une table si elle n'existe pas
        # SQL command to create a table if it does not exist
        cur.execute('''
        CREATE TABLE IF NOT EXISTS Article_Thread (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_Thread VARCHAR(500) NOT NULL,
            User VARCHAR(500) NOT NULL,
            Texte VARCHAR(500) NOT NULL,
            Lien_images VARCHAR(500) NOT NULL,
            Lien_video VARCHAR(500) NOT NULL,
            Date_Thread VARCHAR(500) NOT NULL)
            ''')

        # Requêtes SQL
        # SQL queries
        sql_select = 'SELECT id_Thread FROM Article_Thread WHERE id_Thread = %s'
        sql_insert = 'INSERT INTO Article_Thread (id_Thread, User, Texte, Lien_images, Lien_video, Date_Thread) VALUES (%s, %s, %s, %s, %s, %s)'

        # Insertion des données
        # Data insertion
        for donnee in donnees_a_inserer:
            User = donnee[1]
            id_thread = donnee[0]
            cur.execute(sql_select, (id_thread,))
            result = cur.fetchone()

            if result is None:
                # Vérification et conversion de la valeur de Date_Thread
                # Checking and converting the value of Date_Thread
                date_thread = int(donnee[5]) if donnee[5] else 0  

                # Conversion du timestamp en datetime
                date_thread_formatted = datetime.fromtimestamp(date_thread).strftime('%Y-%m-%d %H:%M:%S')

                # Échapper les caractères spéciaux dans le lien vidéo
                # Escape special characters in video link
                lien_video_escaped = quote(donnee[4], safe=':/')

                donnee_with_date = (id_thread,) + donnee[1:4] + (lien_video_escaped,) + (date_thread_formatted,)

                print("Tuple à insérer:", donnee_with_date)

                cur.execute(sql_insert, donnee_with_date)
                print(f"🟩🟩🟩〔 Thread {id_thread} by {User} has been inserted 〕🟩🟩🟩")
            else:
                print(f"🟧🟧🟧〔 The Thread {id_thread} by {User} has already been inserted 〕 🟧🟧🟧")

        # Validation des changements
        # Validation of changes
        conn.commit()
        print("2️⃣〔Recovery is complete 〕2️⃣")

    except mysql.connector.Error as err:
        print(f"🟥🟥🟥〔MySQL error: {err}〕🟥🟥🟥")

    finally:
        # Fermeture de la connexion dans tous les cas (en cas de succès ou d'échec)
        # Closing the connection in all cases (on success or failure)
        if conn and conn.is_connected():
            cur.close()
            conn.close()
            print("3️⃣〔Connection to the Final database is complete〕3️⃣")
            
