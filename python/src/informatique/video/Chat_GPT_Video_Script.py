import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from setting import client
from datetime import datetime, timedelta
from setting import connect_db  # Supposons que cette fonction retourne une connexion à la base de données
import os

def creation_script_video():

  # Assuming setting.py contains the necessary database connection parameters
  from setting import connect_db

  # Connect to the database
  conn = connect_db()
  c = conn.cursor()
  # Calcul de la date d'hier au format YYYY-MM-DD
  date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

  # Exécution de la requête pour récupérer les données datées d'hier
  c.execute('SELECT Video_filtre1, Video_filtre2, Video_filtre3, Video_filtre4, Video_filtre5 FROM Video_filtre WHERE date = %s', (date_du_jour_avant,))

  # Récupération du premier résultat (si disponible)
  resultat = c.fetchone()

  if resultat:
      # Affectation des résultats à des variables
      data1, data2, data3, data4, data5 = resultat

      # Affichage pour confirmer les valeurs
      print("Recup")
  else:
      print("Aucun résultat trouvé pour la date d'hier.")
      # Si aucun résultat n'est trouvé, vous pourriez vouloir initialiser vos variables ici
      data1 = data2 = data3 = data4 = data5 = None

  # Assurez-vous de fermer la connexion à la base de données si vous avez terminé avec elle
  conn = connect_db()
  c = conn.cursor()
  # Vous pouvez maintenant utiliser `data1`, `data2`, `data3`, `data4`, `data5` pour d'autres opérations

  instruction = """Analyse le texte et crée un resumée basée sur la source pour une video  """


  response = client.chat.completions.create(model="gpt-3.5-turbo", # Specify the model
  messages=[
        {"role": "system", "content": instruction },
        {"role": "user", "content": data1}
    ],
      temperature=0,
      top_p=0,
      frequency_penalty=0,
      presence_penalty=0.0
    )

  script_article_1 = str(response.choices[0].message.content)

  response = client.chat.completions.create(model="gpt-3.5-turbo", # Specify the model
  messages=[
        {"role": "system", "content": instruction },
        {"role": "user", "content": data2}
    ],
      temperature=0,
      top_p=0,
      frequency_penalty=0,
      presence_penalty=0.0
    )

  script_article_2 = str(response.choices[0].message.content)


  response = client.chat.completions.create(model="gpt-3.5-turbo", # Specify the model
  messages=[
        {"role": "system", "content": instruction },
        {"role": "user", "content": data3}
    ],
      temperature=0,
      top_p=0,
      frequency_penalty=0,
      presence_penalty=0.0
    )

  script_article_3 = str(response.choices[0].message.content)

  response = client.chat.completions.create(model="gpt-3.5-turbo", # Specify the model
  messages=[
        {"role": "system", "content": instruction },
        {"role": "user", "content": data4}
    ],
      temperature=0,
      top_p=0,
      frequency_penalty=0,
      presence_penalty=0.0
    )

  script_article_4 = str(response.choices[0].message.content)

  response = client.chat.completions.create(model="gpt-3.5-turbo", # Specify the model
  messages=[
        {"role": "system", "content": instruction },
        {"role": "user", "content": data5}
    ],
      temperature=0,
      top_p=0,
      frequency_penalty=0,
      presence_penalty=0.0
    )

  script_article_5 = str(response.choices[0].message.content)







  c = conn.cursor()

  # Crée la table Article_Filtre si elle n'existe pas
  c.execute('''
  CREATE TABLE IF NOT EXISTS Video_script (
      id INT AUTO_INCREMENT PRIMARY KEY,
      date VARCHAR(10),
      script_article_1 TEXT,
      script_article_2 TEXT,
      script_article_3 TEXT,
      script_article_4 TEXT,
      script_article_5 TEXT
      )
  ''')
  c = conn.cursor()


  # Calcul de la date d'hier au format YYYY-MM-DD
  date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')


  # Vérifie si un enregistrement avec la date d'hier existe déjà
  c.execute('SELECT * FROM Video_script WHERE date = %s', (date_du_jour_avant,))
  if c.fetchone() is None:
      # Insère les données dans la base de données si aucun enregistrement n'existe pour cette date
      c.execute('INSERT INTO Video_script (date, script_article_1, script_article_2, script_article_3, script_article_4, script_article_5) VALUES (%s, %s, %s, %s, %s, %s)', (date_du_jour_avant, script_article_1, script_article_2, script_article_3, script_article_4, script_article_5))
      conn.commit()
      print("Enregistrement ajouté avec succès.")
  else:
      print("Un enregistrement existe déjà pour cette date, aucun nouvel enregistrement n'a été ajouté.")

  # Ferme la connexion à la base de données
  conn.close()


  # Calcul de la date du jour avant et conversion en chaîne de caractères
  date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

  # Emplacement du dossier à créer, incluant la date calculée
  chemin_dossier = f"./python/data/veille_video/veille_du_{date_du_jour_avant}"

  scripts = [script_article_1, script_article_2, script_article_3, script_article_4]

  # Création du dossier s'il n'existe pas
  if not os.path.exists(chemin_dossier):
      os.makedirs(chemin_dossier)
      print(f"Le dossier '{chemin_dossier}' a été créé.")
  else:
      print(f"Le dossier '{chemin_dossier}' existe déjà.")

  for i, script in enumerate(scripts, start=1):
      chemin_fichier = os.path.join(chemin_dossier, f"script_article_{i}.txt")
      with open(chemin_fichier, "w") as fichier:
          fichier.write(script)
      print(f"Le fichier 'script_article_{i}.txt' a été créé dans '{chemin_dossier}'.")

  print("4 fichiers texte ont été créés dans le dossier spécifié avec le contenu spécifique.")
