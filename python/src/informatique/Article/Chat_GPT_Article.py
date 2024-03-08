import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from setting import client
from source import Source
from datetime import datetime, timedelta
from setting import connect_db
conn = connect_db()



def generer_article_veille():

    c = conn.cursor()

# Calcul de la date d'hier au format YYYY-MM-DD
    date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

# Exécution de la requête pour récupérer le Filtre_resultat daté d'hier
    c.execute('SELECT Filtre_resultat FROM Article_Filtre WHERE date = %s', (date_du_jour_avant,))

# Récupération des résultats
    resultats = c.fetchall()

# Transformer le résultat en chaîne de caractères et l'afficher
    if resultats:
        resultat_en_string = str(resultats[0][0])  # Convertit le premier (et unique) résultat en string
        print(resultat_en_string)
    else:
        print("Aucun résultat trouvé pour la date d'hier.")








    data = resultat_en_string

    instruction = """
Bonjour je m’appelle dycon est tu es programme qui récupère des textes et tu dois les analyser et créer un résumé dans un article de veille informatique 
it is very important that it does not exceed 1900 characters 
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


    response = client.chat.completions.create(model="gpt-4", # Specify the model
    messages=[
          {"role": "system", "content": instruction },
          {"role": "user", "content": data}
      ],
        temperature=0,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0.0,
        max_tokens=2000 # Limite de tokens pour la réponse

      )

    result_article = str(response.choices[0].message.content)


    c = conn.cursor()

    # Crée la table Article_Filtre si elle n'existe pas
    c.execute('''
        CREATE TABLE IF NOT EXISTS Article_final (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Article_resultat TEXT,
            date VARCHAR(10)
        )
    ''')

# Vérifie si un enregistrement avec la date d'hier existe déjà
    c.execute('SELECT * FROM Article_final WHERE date = %s', (date_du_jour_avant,))
    if c.fetchone() is None:
    # Insère les données dans la base de données si aucun enregistrement n'existe pour cette date
        c.execute('INSERT INTO Article_final (Article_resultat, date) VALUES (%s, %s)', (result_article, date_du_jour_avant))
        conn.commit()
        print("Enregistrement ajouté avec succès.")
    else:
        print("Un enregistrement existe déjà pour cette date, aucun nouvel enregistrement n'a été ajouté.")

# Ferme la connexion à la base de données
    conn.close()

