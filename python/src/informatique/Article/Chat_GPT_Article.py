import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from setting import client
from setting import LANGUAGE

from datetime import datetime, timedelta
from setting import connect_db
conn = connect_db()



def generer_article_veille():

    c = conn.cursor()

# Calcul de la date d'hier au format YYYY-MM-DD
# Calculation of yesterday's date in YYYY-MM-DD format
    date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

# Exécution de la requête pour récupérer le Filtre_resultat daté d'hier
# Execution of the query to retrieve the Filter_result dated yesterday    
    c.execute('SELECT Filtre_resultat FROM Article_Filtre WHERE date = %s', (date_du_jour_avant,))

# Récupération des résultats
    resultats = c.fetchall()

# Transformer le résultat en chaîne de caractères et l'afficher
# Transform the result into a string and display it
    if resultats:
        resultat_en_string = str(resultats[0][0])  
        print(resultat_en_string)
    else:
        print("No results found for yesterday's date")








    data = resultat_en_string

    instruction = f"""
Bonjour je m’appelle dycon est tu es programme qui récupère des textes et tu dois les analyser et créer un résumé en {LANGUAGE} dans un article de veille informatique 
Pour créer l’article suis cette template

(Utilise Pas de lien)

☕️ Hello There, Bienvenue sur m’a veille technologique voici différentes info sur ce qui c’est passé hier 

[Emoji avec un lien de l’article] Resumé de l’article 

🔗 Sources :
[Inclure ici la liste complète des nom  source]

🗣️ Votre Avis  Qu’en pensez-vous ? 

📱N'hésitez pas à partager vos propres découvertes ou à poser des questions. La veille technologique est un voyage collectif!

#VeilleInformatique #Technologie #Innovation #SécuritéInformatique #AI #ML
[Insérer plusieurs hashtag lié au sujet]
Restez connectés pour plus d'informations demain!
"""


    response = client.chat.completions.create(model="gpt-4", 
    messages=[
          {"role": "system", "content": instruction },
          {"role": "user", "content": data}
      ],
        temperature=0,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0.0,

      )

    result_article = str(response.choices[0].message.content)


    c = conn.cursor()

    # Crée la table Article_Filtre si elle n'existe pas
    # Creates the Article_Filter table if it does not exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS Article_final (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Article_resultat TEXT,
            date VARCHAR(10)
        )
    ''')

# Vérifie si un enregistrement avec la date d'hier existe déjà
# Checks if a record with yesterday's date already exists
    c.execute('SELECT * FROM Article_final WHERE date = %s', (date_du_jour_avant,))
    if c.fetchone() is None:
    # Insère les données dans la base de données si aucun enregistrement n'existe pour cette date
    # Insert data into database if no records exist for this date
        c.execute('INSERT INTO Article_final (Article_resultat, date) VALUES (%s, %s)', (result_article, date_du_jour_avant))
        conn.commit()
        print("🟩Record added successfully.🟩")
    else:
        print("🟧A record already exists for this date, no new records have been added.🟧")

# Ferme la connexion à la base de données
# Close the database connection
    conn.close()

