import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from setting import client
from datetime import datetime, timedelta
from setting import connect_db  # Supposons que cette fonction retourne une connexion à la base de données

from source import Source

# Assuming setting.py contains the necessary database connection parameters
from setting import connect_db

def création_mot_video():

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

  instruction = """crée 1 mot clée tres generique en anglais  liée a cette article """


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

  mots_clée_1 = str(response.choices[0].message.content)

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

  mots_clée_2 = str(response.choices[0].message.content)


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

  mots_clée_3 = str(response.choices[0].message.content)

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

  mots_clée_4 = str(response.choices[0].message.content)

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

  mots_clée_5 = str(response.choices[0].message.content)







  c = conn.cursor()

  # Crée la table Article_Filtre si elle n'existe pas
  c.execute('''
  CREATE TABLE IF NOT EXISTS Video_mots (
      id INT AUTO_INCREMENT PRIMARY KEY,
      date VARCHAR(10),
      mots_clée_1 TEXT,
      mots_clée_2 TEXT,
      mots_clée_3 TEXT,
      mots_clée_4 TEXT,
      mots_clée_5 TEXT
      )
  ''')
  c = conn.cursor()


  # Calcul de la date d'hier au format YYYY-MM-DD
  date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')


  # Vérifie si un enregistrement avec la date d'hier existe déjà
  c.execute('SELECT * FROM Video_mots WHERE date = %s', (date_du_jour_avant,))
  if c.fetchone() is None:
      # Insère les données dans la base de données si aucun enregistrement n'existe pour cette date
      c.execute('INSERT INTO Video_mots (date, mots_clée_1, mots_clée_2, mots_clée_3, mots_clée_4, mots_clée_5) VALUES (%s, %s, %s, %s, %s, %s)', (date_du_jour_avant, mots_clée_1, mots_clée_2, mots_clée_3, mots_clée_4, mots_clée_5))
      conn.commit()
      print("Enregistrement ajouté avec succès.")
  else:
      print("Un enregistrement existe déjà pour cette date, aucun nouvel enregistrement n'a été ajouté.")

  # Ferme la connexion à la base de données
  conn.close()





