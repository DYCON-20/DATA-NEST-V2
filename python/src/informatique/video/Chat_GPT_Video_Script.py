import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from setting import client
from datetime import datetime, timedelta
from setting import connect_db  
import os

from setting import Theme


datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

def creation_script_video():
  print("creation_script_video")


  from setting import connect_db

  conn = connect_db()
  c = conn.cursor()
  date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

  c.execute('SELECT Video_filtre1, Video_filtre2, Video_filtre3, Video_filtre4, Video_filtre5 FROM Video_filtre WHERE date = %s', (date_du_jour_avant,))

  resultat = c.fetchone()

  if resultat:
      data1, data2, data3, data4, data5 = resultat
      print("Recup")
  else:
      print("Aucun résultat trouvé pour la date d'hier.")
      data1 = data2 = data3 = data4 = data5 = None

  conn = connect_db()
  c = conn.cursor()

  instruction = """Analyzes the text and creates a summary in French based on the source to create the text of a video Das se format ne mes pas les (")
it is very important that it does not exceed
  180 characters 



""to summarize"" 

"""


  response = client.chat.completions.create(
    model="gpt-3.5-turbo", 
    messages=[
      {"role": "system", "content": instruction},
      {"role": "user", "content": data1}
    ],
    max_tokens=50, 
    temperature=0,
    top_p=1, 
    frequency_penalty=0,
    presence_penalty=0.0
  )


  script_article_1 = str(response.choices[0].message.content)

  response = client.chat.completions.create(
    model="gpt-3.5-turbo", 
    messages=[
      {"role": "system", "content": instruction},
      {"role": "user", "content": data2}
    ],
    max_tokens=50, 
    temperature=0,
    top_p=1, 
    frequency_penalty=0,
    presence_penalty=0.0
  )


  script_article_2 = str(response.choices[0].message.content)


  response = client.chat.completions.create(
    model="gpt-3.5-turbo", 
    messages=[
      {"role": "system", "content": instruction},
      {"role": "user", "content": data3}
    ],
    max_tokens=50, 
    temperature=0,
    top_p=1, 
    frequency_penalty=0,
    presence_penalty=0.0
  )


  script_article_3 = str(response.choices[0].message.content)

  response = client.chat.completions.create(
    model="gpt-3.5-turbo", 
    messages=[
      {"role": "system", "content": instruction},
      {"role": "user", "content": data4}
    ],
    max_tokens=50, 
    temperature=0,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.0
  )


  script_article_4 = str(response.choices[0].message.content)

  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": instruction},
      {"role": "user", "content": data5}
    ],
    max_tokens=50, 
    temperature=0,
    top_p=1, 
    frequency_penalty=0,
    presence_penalty=0.0
  )


  script_article_5 = str(response.choices[0].message.content)







  c = conn.cursor()


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

  date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')


  c.execute('SELECT * FROM Video_script WHERE date = %s', (date_du_jour_avant,))
  if c.fetchone() is None:
      c.execute('INSERT INTO Video_script (date, script_article_1, script_article_2, script_article_3, script_article_4, script_article_5) VALUES (%s, %s, %s, %s, %s, %s)', (date_du_jour_avant, script_article_1, script_article_2, script_article_3, script_article_4, script_article_5))
      conn.commit()
      print("Enregistrement ajouté avec succès.")
  else:
      print("Un enregistrement existe déjà pour cette date, aucun nouvel enregistrement n'a été ajouté.")

  conn.close()


  date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

  chemin_dossier = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/subtitle"

  scripts = [script_article_1, script_article_2, script_article_3, script_article_4]

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
pass