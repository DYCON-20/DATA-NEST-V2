import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Setting.setting import  client
from datetime import datetime, timedelta
from Setting.setting import  connect_db  
import os
from Setting.setting import  LANGUAGE

from Setting.setting import  Theme


datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

def creation_script_video():
  try:

    print("-")
    print("🟦 Create the 5 scripts for the video [ B{4/10} ]🟦")


    from Setting.setting import  connect_db

    conn = connect_db()
    c = conn.cursor()
    date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    c.execute('SELECT Video_filtre1, Video_filtre2, Video_filtre3, Video_filtre4, Video_filtre5 FROM Video_filtre WHERE date = %s', (date_du_jour_avant,))

    resultat = c.fetchone()

    if resultat:
        data1, data2, data3, data4, data5 = resultat
        print("to recover")
    else:
        print("❌No results found for yesterday's date.❌")
        data1 = data2 = data3 = data4 = data5 = None

    conn = connect_db()
    c = conn.cursor()

    instruction = f"""You are a technology monitoring journalist, you speak in a video about a new article

  Analyze the text and Generate a script for a video, in {LANGUAGE} based on the source to create the text of a video In this format I don't have them
  it is very important that it does not exceed 180 characters
  it is very important that it does not exceed 180 characters


    The script should be returned as a string with the specified number of paragraphs.
                  Here is an example string:
                  "This is an example of a string."

                  Do not refer to this prompt in any way in your response.
                  Get straight to the point, don't start with unnecessary things like "welcome to this video".

                  Obviously, the script must be related to the subject of the video.

                  YOU MUST NOT INCLUDE ANY TYPE OF MARKDOWN OR FORMATTING IN THE SCRIPT, NEVER USE A TITLE Or @ or link
                  RETURN ONLY THE RAW SCRIPT CONTENT. DO NOT INCLUDE “VOICE OVER,” “NARRATOR,” OR SIMILAR INDICATORS OF WHAT SHOULD BE SPOKEN AT THE BEGINNING OF EACH PARAGRAPH OR LINE. YOU MUST NOT MENTION THE PROMPT OR ANYTHING ABOUT THE SCRIPT ITSELF. ALSO, NEVER TALK ABOUT THE NUMBER OF PARAGRAPHS OR LINES. JUST WRITE THE SCRIPT.

  it is very important that it does not exceed 180 characters
  it is very important that it does not exceed 180 characters
  

  """


    response = client.chat.completions.create(
      model="gpt-4", 
      messages=[
        {"role": "system", "content": instruction},
        {"role": "user", "content": data1}
      ],
      max_tokens=200, 
      temperature=0,
      top_p=1, 
      frequency_penalty=0,
      presence_penalty=0.0
    )


    script_article_1 = str(response.choices[0].message.content)

    response = client.chat.completions.create(
      model="gpt-4", 
      messages=[
        {"role": "system", "content": instruction},
        {"role": "user", "content": data2}
      ],
      max_tokens=200, 
      temperature=0,
      top_p=1, 
      frequency_penalty=0,
      presence_penalty=0.0
    )


    script_article_2 = str(response.choices[0].message.content)


    response = client.chat.completions.create(
      model="gpt-4", 
      messages=[
        {"role": "system", "content": instruction},
        {"role": "user", "content": data3}
      ],
      max_tokens=200, 
      temperature=0,
      top_p=1, 
      frequency_penalty=0,
      presence_penalty=0.0
    )


    script_article_3 = str(response.choices[0].message.content)

    response = client.chat.completions.create(
      model="gpt-4", 
      messages=[
        {"role": "system", "content": instruction},
        {"role": "user", "content": data4}
      ],
      max_tokens=200, 
      temperature=0,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.0
    )


    script_article_4 = str(response.choices[0].message.content)

    response = client.chat.completions.create(
      model="gpt-4",
      messages=[
        {"role": "system", "content": instruction},
        {"role": "user", "content": data5}
      ],
      max_tokens=200, 
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
        print("🟩Record added successfully.🟩")
    else:
        print("🟧A record already exists for this date, no new records have been added.🟧")

    conn.close()


    date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    chemin_dossier = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/subtitle"

    scripts = [script_article_1, script_article_2, script_article_3, script_article_4]

    if not os.path.exists(chemin_dossier):
        os.makedirs(chemin_dossier)
        print(f"🟩The folder '{chemin_dossier}' has been created🟩")
    else:
        print(f"🟧The folder'{chemin_dossier}' already exists🟧")

    for i, script in enumerate(scripts, start=1):
        chemin_fichier = os.path.join(chemin_dossier, f"script_article_{i}.txt")
        with open(chemin_fichier, "w") as fichier:
            fichier.write(script)
        print(f"🟫the file'script_article_{i}.txt'was created in '{chemin_dossier}🟫'.")

    print("4 text files were created in the specified folder with the specific content.")  
  except Exception as e:
            print(f"""❌❌An error has occurred (Create the 5 scripts for the video) ❌❌
            ➡️Here is the error message 🟨{e}🟨 """)
