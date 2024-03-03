import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from pathlib import Path
from setting import client
from datetime import datetime, timedelta
from setting import connect_db
conn = connect_db()
from source import Source

# Assuming setting.py contains the necessary database connection parameters
from setting import connect_db




def creation_filtre_video():
    data = Source
    conn = connect_db()
    c = conn.cursor()

    instruction = '''Filtre et affiche seulement 5 articles pour une veille informatique 
    la réponse doit être structurée comme :


    articles 1 

    articles 2 

    articles 3 

    articles 4 

    articles 5 

    ''' 

    response = client.chat.completions.create(model="gpt-3.5-turbo", # Specify the model
    messages=[
        {"role": "system", "content": instruction },
        {"role": "user", "content": data}
    ],
        temperature=0,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0.0
    )

    result_filtre_video = str(response.choices[0].message.content)

    # Split the response to get individual articles
    delimiter = "\n\n"  # Update this based on the actual response format
    articles = result_filtre_video.strip().split(delimiter)

    if len(articles) >= 5:
        # Store articles
        article_1 = articles[0]
        article_2 = articles[1]
        article_3 = articles[2]
        article_4 = articles[3]
        article_5 = articles[4]

        # Insert into database
        date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

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

        c.execute('SELECT * FROM Video_filtre WHERE date = %s', (date_du_jour_avant,))
        if c.fetchone() is None:
            c.execute('INSERT INTO Video_filtre (date, Video_filtre1, Video_filtre2, Video_filtre3, Video_filtre4, Video_filtre5) VALUES (%s, %s, %s, %s, %s, %s)', 
            (date_du_jour_avant, article_1, article_2, article_3, article_4, article_5))
            conn.commit()
            print("Enregistrement ajouté avec succès.")
        else:
            print("Un enregistrement existe déjà pour cette date, aucun nouvel enregistrement n'a été ajouté.")
    else:
        print("Not enough articles found. Found only:", len(articles))

    # Close the database connection
    conn.close()

# Make sure to call your function where appropriate