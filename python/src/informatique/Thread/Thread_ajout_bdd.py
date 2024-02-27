import mysql.connector
from datetime import datetime
from urllib.parse import quote

#local
from local import connect_db


def recuperationbdd(donnees_a_inserer):

    try:
        conn = connect_db()

   
        if conn.is_connected():
            print("Connexion à la base de données MySQL établie.")

        # Création d'un curseur
        cur = conn.cursor()

        # Commande SQL pour créer une table si elle n'existe pas
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
        sql_select = 'SELECT id_Thread FROM Article_Thread WHERE id_Thread = %s'
        sql_insert = 'INSERT INTO Article_Thread (id_Thread, User, Texte, Lien_images, Lien_video, Date_Thread) VALUES (%s, %s, %s, %s, %s, %s)'

        # Insertion des données
        for donnee in donnees_a_inserer:
            id_thread = donnee[0]
            cur.execute(sql_select, (id_thread,))
            result = cur.fetchone()

            if result is None:
                # Vérification et conversion de la valeur de Date_Thread
                date_thread = int(donnee[5]) if donnee[5] else 0  

                # Conversion du timestamp en datetime
                date_thread_formatted = datetime.fromtimestamp(date_thread).strftime('%Y-%m-%d %H:%M:%S')

                # Échapper les caractères spéciaux dans le lien vidéo
                lien_video_escaped = quote(donnee[4], safe=':/')

                donnee_with_date = (id_thread,) + donnee[1:4] + (lien_video_escaped,) + (date_thread_formatted,)

                print("Tuple à insérer:", donnee_with_date)

                cur.execute(sql_insert, donnee_with_date)
                print(f"Données pour id_Thread {id_thread} insérées avec succès.✅")
            else:
                print(f"id_Thread {id_thread} existe déjà, les données ne sont pas insérées.📍")

        # Validation des changements
        conn.commit()
        print("Opération terminée avec succès.✅")

    except mysql.connector.Error as err:
        print(f"Erreur MySQL: {err}⚠️🛑🛑🛑")

    finally:
        # Fermeture de la connexion dans tous les cas (en cas de succès ou d'échec)
        if conn and conn.is_connected():
            cur.close()
            conn.close()
            print("Connexion à la base de données MySQL fermée.")

# Exemple d'utilisation
donnees_a_inserer = [
    ('3288164974458941110_1591732793', 'lesnumeriques', "Si vous en avez marre des casques pour jouer à la PS5, Sony a pensé à vous avec les Pulse Explore. Attention, on a pas dit qu'ils étaient bien par contre.", '', 'https://scontent.cdninstagram.com/v/t66.30100-16/10000000_345849955019336_3429142815092431005_n.mp4?efg=e30&_nc_ht=scontent.cdninstagram.com&_nc_cat=108&_nc_ohc=YlTKlMsq-NcAX_1dEcr&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfD0ROO77WwIMpEHQR2M298qRE7oILlLgHk_SaNyXnRq0g&oe=65B8A7A8&_nc_sid=10d13b', 1706199944),
    # Ajoutez d'autres données ici si nécessaire
]

recuperationbdd(donnees_a_inserer)
