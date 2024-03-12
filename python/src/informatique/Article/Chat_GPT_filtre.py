import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from setting import client
from source import Source
from datetime import datetime, timedelta
from setting import connect_db
conn = connect_db()

def generer_filtre_veille():

    data = Source

    instruction = """Filtre et affiche par ordre du plus interresant au moin interresant  seulement les articles correspondant à ces critères : - Lié à l’informatique et à la technologie - Pas une pub (un podcast, une vidéo) - Nouveauté ou événement - Affiche les données avec cette template : User Texte Pas de lien
    la réponse doit être structurée comme :


    articles i 

    articles i 

    articles i 

    articles i 

    articles i 
    
    ....
    """

    response = client.chat.completions.create(model="gpt-4", # Specify the model
    messages=[
          {"role": "system", "content": instruction },
          {"role": "user", "content": data}
      ],
       temperature=0,
        top_p=0,
       frequency_penalty=0,
       presence_penalty=0.0
     )

    result_filtre = str(response.choices[0].message.content)
    print(result_filtre)

# Calcule la date du jour précédent
    date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')


    c = conn.cursor()

# Crée la table Article_Filtre si elle n'existe pas
    c.execute('''
        CREATE TABLE IF NOT EXISTS Article_Filtre (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Filtre_resultat TEXT,
            date VARCHAR(10)
        )
    ''')

# Vérifie si un enregistrement avec la date d'hier existe déjà
    c.execute('SELECT * FROM Article_Filtre WHERE date = %s', (date_du_jour_avant,))
    if c.fetchone() is None:
    # Insère les données dans la base de données si aucun enregistrement n'existe pour cette date
        c.execute('INSERT INTO Article_Filtre (Filtre_resultat, date) VALUES (%s, %s)', (result_filtre, date_du_jour_avant))
        conn.commit()
        print("Enregistrement ajouté avec succès.")
    else:
        print("Un enregistrement existe déjà pour cette date, aucun nouvel enregistrement n'a été ajouté.")

# Ferme la connexion à la base de données

    articles = result_filtre.strip().split("\n\nArticle ")
    articles = [article.split(": \n\n", 1)[1] if ": \n\n" in article else article for article in articles]
    
    if len(articles) < 5:
        print(f"Not enough articles found. Found only: {len(articles)}")
        return
    
    # Extraction des 5 premiers articles
    articles_selectionnes = articles[:5]
    
    # Formatage de la date du jour précédent
    date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
 
    
    # Création de la table si elle n'existe pas
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
    c.execute('SELECT * FROM Video_filtre WHERE date = %s', (date_du_jour_avant,))
    if c.fetchone() is None:
        # Insérer les données
        c.execute('INSERT INTO Video_filtre (date, Video_filtre1, Video_filtre2, Video_filtre3, Video_filtre4, Video_filtre5) VALUES (%s, %s, %s, %s, %s, %s)', 
                  (date_du_jour_avant, *articles_selectionnes))
        conn.commit()
        print("Enregistrement ajouté avec succès.")
    else:
        print("Un enregistrement existe déjà pour cette date. Aucun nouvel enregistrement n'a été ajouté.")
    
    # Fermeture de la connexion
    conn.close()

generer_filtre_veille()