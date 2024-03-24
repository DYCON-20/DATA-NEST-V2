from Setting.setting import  connect_db
from datetime import datetime, timedelta

def Source():
    # Établissement de la connexion
    conn = connect_db()
    cursor = conn.cursor()

    # Création de la table Sources si elle n'existe pas
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Sources (
        ID SERIAL PRIMARY KEY,
        Date DATE NOT NULL,
        Content TEXT NOT NULL
    )
    """
    cursor.execute(create_table_query)

    # Validation de la création de la table
    conn.commit()

    # Calcul de la date du jour d'avant
    yesterday_date = datetime.now() - timedelta(1)
    yesterday_str = yesterday_date.strftime('%Y-%m-%d')

    # Vérification de l'existence d'une entrée pour cette date
    cursor.execute("SELECT * FROM Sources WHERE Date = %s", (yesterday_str,))
    if cursor.fetchone() is None:
        # Aucune entrée pour cette date, procéder à l'insertion

        # Sélection et affichage des threads du jour d'avant
        cursor.execute("SELECT User, Texte FROM Article_Thread WHERE Date_Thread LIKE %s", (yesterday_str + '%',))
        yesterday_date_threads_resultat = cursor.fetchall()

        # Préparation de la chaîne à insérer
        source_content = "IT monitoring from " + yesterday_str + " Thread = " + str(yesterday_date_threads_resultat)
        # Insertion dans la base de données
        insert_query = "INSERT INTO Sources (Date, Content) VALUES (%s, %s)"
        cursor.execute(insert_query, (yesterday_str, source_content))

        # Validation de l'insertion
        conn.commit()
    else:
        # Une entrée existe déjà pour cette date, aucune action requise
        print("Une entrée existe déjà pour la date", yesterday_str)

    # Fermeture de la connexion
    conn.close()

