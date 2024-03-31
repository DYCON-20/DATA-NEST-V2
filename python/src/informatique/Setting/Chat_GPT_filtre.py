import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Setting.setting import  client
from Setting.source import Source
from datetime import datetime, timedelta
from Setting.setting import  connect_db
conn = connect_db()
import re
def generer_filtre_veille():
    try:
        print("-")
        print(" 🟪 Create filtre  🟪 ")

        conn = connect_db()
        cursor = conn.cursor()
        yesterday_date = datetime.now() - timedelta(1)
        yesterday_str = yesterday_date.strftime('%Y-%m-%d')
        
        cursor.execute("SELECT Content FROM Sources WHERE Date LIKE %s", (yesterday_str + '%',))
        Source = cursor.fetchall()

        print(" 🟪🟦Filter the sources to keep the essentials for the article and also save them separately [ A{1/2} B{1/10} ]🟦🟪 ")

        data = Source
        data_converted = str(data)

        instruction = """Filtre et affiche par ordre du plus interresant au moin interresant  seulement les articles correspondant à ces critères : - Lié à l’informatique et à la technologie - Pas une pub (un podcast, une vidéo) - Nouveauté ou événement - Affiche les données avec cette template : User Texte Pas de lien
        la réponse doit être structurée comme :


        articles i 
        {texte}
        Source 
        {Source}

        articles i 
        {texte}
        Source 
        {Source}


        articles i 
        {texte}
        Source 
        {Source}

        articles i 
        {texte}
        Source 
        {Source}

        articles i 
        {texte}
        Source 
        {Source}
        ....
        """

        response = client.chat.completions.create(model="gpt-4", 
        messages=[
            {"role": "system", "content": instruction },
            {"role": "user", "content": data_converted}
        ],
        temperature=0,
            top_p=0,
        frequency_penalty=0,
        presence_penalty=0.0
        )

        result_filtre = str(response.choices[0].message.content)
        print(result_filtre)

    # Calcule la date du jour précédent
    # Calculates the date of the previous day
        date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')


        c = conn.cursor()

    # Crée la table Article_Filtre si elle n'existe pas
    # Creates the Article_Filter table if it does not exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS Article_Filtre (
                id INT AUTO_INCREMENT PRIMARY KEY,
                Filtre_resultat TEXT,
                date VARCHAR(10)
            )
        ''')

    # Vérifie si un enregistrement avec la date d'hier existe déjà
    # Checks if a record with yesterday's date already exists
        c.execute('SELECT * FROM Article_Filtre WHERE date = %s', (date_du_jour_avant,))
        if c.fetchone() is None:
        # Insère les données dans la base de données si aucun enregistrement n'existe pour cette date
        # Insert data into database if no records exist for this date
            c.execute('INSERT INTO Article_Filtre (Filtre_resultat, date) VALUES (%s, %s)', (result_filtre, date_du_jour_avant))
            conn.commit()
            print("Enregistrement ajouté avec succès.")
        else:
            print("Un enregistrement existe déjà pour cette date, aucun nouvel enregistrement n'a été ajouté.")

        articles = result_filtre.strip().split("\n\nArticle ")
        articles = [article.split(": \n\n", 1)[1] if ": \n\n" in article else article for article in articles]
        articles = [article.split("Source:")[0].strip() for article in articles]

        if len(articles) < 5:
            print(f"Not enough articles found. Found only: {len(articles)}")
            return
        
        # Extraction des 5 premiers articles
        # Extraction of the first 5 articles
        articles_selectionnes = articles[:5]
        
        # Formatage de la date du jour précédent
        # Formatting the previous day's date
        date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        
    
        
        # Création de la table si elle n'existe pas
        # Creation of the table if it does not exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS Video_filtre (
                id INT AUTO_INCREMENT PRIMARY KEY,
                date VARCHAR(10),
                Video_filtre1 TEXT,
                Video_filtre2 TEXT,
                Video_filtre3 TEXT,
                Video_filtre4 TEXT,
                Video_filtre5 TEXT
            )
        ''')
        
        # Vérification de l'existence d'un enregistrement pour la date du jour précédent
        # Checking for the existence of a record for the previous day's date
        c.execute('SELECT * FROM Video_filtre WHERE date = %s', (date_du_jour_avant,))
        if c.fetchone() is None:
            # Insérer les données
            c.execute('INSERT INTO Video_filtre (date, Video_filtre1, Video_filtre2, Video_filtre3, Video_filtre4, Video_filtre5) VALUES (%s, %s, %s, %s, %s, %s)', 
                    (date_du_jour_avant, *articles_selectionnes))
            conn.commit()
            print("Enregistrement ajouté avec succès.")
        else:
            print("Un enregistrement existe déjà pour cette date. Aucun nouvel enregistrement n'a été ajouté.")
                



        # Extraction de la source pour chaque article en utilisant une expression régulière
        pattern = re.compile(r"Source\n(.+)|Source: (.+)")
        matches = pattern.findall(result_filtre)

        # Nettoyage des résultats pour ne garder qu'une source par match
        sources = [match[0] if match[0] else match[1] for match in matches]

        if len(sources) < 5:
            print(f"Not enough sources found. Found only: {len(sources)}")
        else:
            # Sélection des 5 premières sources
            sources_selectionnees = sources[:5]

            # Formatage de la date du jour précédent
            date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

            # Création de la table si elle n'existe pas
            c.execute('''
                CREATE TABLE IF NOT EXISTS Source_filtre (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    date VARCHAR(10),
                    Source_filtre1 TEXT,
                    Source_filtre2 TEXT,
                    Source_filtre3 TEXT,
                    Source_filtre4 TEXT,
                    Source_filtre5 TEXT
                )
            ''')

            # Vérification de l'existence d'un enregistrement pour la date du jour précédent
            c.execute('SELECT * FROM Source_filtre WHERE date = %s', (date_du_jour_avant,))
            if c.fetchone() is None:
                # Insérer les données des sources
                c.execute('INSERT INTO Source_filtre (date, Source_filtre1, Source_filtre2, Source_filtre3, Source_filtre4, Source_filtre5) VALUES (%s, %s, %s, %s, %s, %s)', 
                        (date_du_jour_avant, *sources_selectionnees))
                conn.commit()
                print("Enregistrement ajouté avec succès.")
            else:
                print("Un enregistrement existe déjà pour cette date. Aucun nouvel enregistrement n'a été ajouté.")


    except Exception as e:
            print(f"""❌❌An error has occurred ❌❌
            The most common errors are 
            -⚠️Does your API key work? 
            -⚠️Is the connection to your database working correctly?  
	        -⚠️check the return of the item
            ➡️Here is the error message 🟨{e}🟨 """)

