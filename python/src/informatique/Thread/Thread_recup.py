from local import connect_db
from datetime import datetime, timedelta

# Établissement de la connexion
conn = connect_db()
cursor = conn.cursor()

# Calcul de la date du jour d'avant
yesterday_date = datetime.now() - timedelta(1)
yesterday_str = yesterday_date.strftime('%Y-%m-%d')

# Sélection et affichage des threads du jour d'avant
cursor.execute("SELECT * FROM Article_Thread WHERE Date_Thread LIKE %s", (yesterday_str + '%',))

threads_resultat = cursor.fetchall()

# Conversion du résultat en string
threads_resultat_str = str(threads_resultat)

# Affichage du résultat sous forme de string
print(threads_resultat_str)

# Fermeture de la connexion
conn.close()
