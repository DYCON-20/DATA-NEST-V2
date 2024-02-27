from setting import connect_db
from datetime import datetime, timedelta

# Établissement de la connexion
conn = connect_db()
cursor = conn.cursor()

# Calcul de la date du jour d'avant
yesterday_date = datetime.now() - timedelta(1)
yesterday_str = yesterday_date.strftime('%Y-%m-%d')

# Sélection et affichage des threads du jour d'avant
cursor.execute("SELECT USER,Texte FROM Article_Thread WHERE Date_Thread LIKE %s", (yesterday_str + '%',))

yesterday_date_threads_resultat = cursor.fetchall()

# Conversion du résultat en string
yesterday_date_threads_resultat = str(yesterday_date_threads_resultat)

# Affichage du résultat sous forme de string

conn.close()

Source = "IT monitoring from "+ yesterday_str + " Tread = " + yesterday_date_threads_resultat 

#print(Source)