import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Setting.setting import  client
from datetime import datetime, timedelta
from Setting.setting import  connect_db  

from Setting.source import Source

from Setting.setting import  connect_db

def creation_word_video():
  try:

    print("-")
    print("🟦 filter and create keywords for videos [ B{3/10} ]🟦")

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

    instruction = """gives a single word which corresponds most to this article according to this corpus of words in English if nothing corresponds displays the most adaptable word (Computer, Server, Hard disk, Motherboard, Processor, Graphics card, Keyboard, Mouse, Monitor, Laptop, Operating system, database, web browser, mobile application, programming software, artificial intelligence, neural network, network, Internet, cloud computing, cybersecurity, cryptography, blockchain, data center, Wi-Fi, Ethernet , VPN, code, software development, application Programming interface, GitHub, Containerization, Virtualization, Agile, Scrum, Big Data, Machine Learning, Deep Learning, IoT (Internet of Things), Augmented Reality, Virtual Reality, Robotics, Drones, Hacking , Software bug, Benchmark, Overclocking, 3D modeling, 3D printing, E-sports, Video game"""


    response = client.chat.completions.create(model="gpt-3.5-turbo", 
    messages=[
          {"role": "system", "content": instruction },
          {"role": "user", "content": data1}
      ],
        temperature=0,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0.0
      )

    mots_clee_1 = str(response.choices[0].message.content)

    response = client.chat.completions.create(model="gpt-3.5-turbo", 
    messages=[
          {"role": "system", "content": instruction },
          {"role": "user", "content": data2}
      ],
        temperature=0,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0.0
      )

    mots_clee_2 = str(response.choices[0].message.content)


    response = client.chat.completions.create(model="gpt-3.5-turbo", 
    messages=[
          {"role": "system", "content": instruction },
          {"role": "user", "content": data3}
      ],
        temperature=0,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0.0
      )

    mots_clee_3 = str(response.choices[0].message.content)

    response = client.chat.completions.create(model="gpt-3.5-turbo", 
    messages=[
          {"role": "system", "content": instruction },
          {"role": "user", "content": data4}
      ],
        temperature=0,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0.0
      )

    mots_clee_4 = str(response.choices[0].message.content)

    response = client.chat.completions.create(model="gpt-3.5-turbo", 
    messages=[
          {"role": "system", "content": instruction },
          {"role": "user", "content": data5}
      ],
        temperature=0,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0.0
      )

    mots_clee_5 = str(response.choices[0].message.content)







    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS Video_mots (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date VARCHAR(10),
        mots_clee_1 TEXT,
        mots_clee_2 TEXT,
        mots_clee_3 TEXT,
        mots_clee_4 TEXT,
        mots_clee_5 TEXT
        )
    ''')
    c = conn.cursor()


    date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')


    c.execute('SELECT * FROM Video_mots WHERE date = %s', (date_du_jour_avant,))
    if c.fetchone() is None:
        c.execute('INSERT INTO Video_mots (date, mots_clee_1, mots_clee_2, mots_clee_3, mots_clee_4, mots_clee_5) VALUES (%s, %s, %s, %s, %s, %s)', (date_du_jour_avant, mots_clee_1, mots_clee_2, mots_clee_3, mots_clee_4, mots_clee_5))
        conn.commit()
        print("🟩Record added successfully.🟩")
    else:
        print("🟧A record already exists for this date, no new records have been added.🟧")

    conn.close()
  except Exception as e:
            print(f"""❌❌An error has occurred() ❌❌
            ➡️Here is the error message 🟨{e}🟨 """)




