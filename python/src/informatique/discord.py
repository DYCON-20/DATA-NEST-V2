import datetime  # Assurez-vous d'importer datetime
from datetime import datetime, timedelta
from setting import connect_db  # Import correct de vos paramètres de connexion
import pysrt
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import random
from datetime import datetime, timedelta
from mutagen.mp3 import MP3

import requests

from setting import WEBHOOK
from setting import Theme


def send_discord():



    # Connexion à la base de données
    conn = connect_db()
    c = conn.cursor()

    # Calcul de la date d'hier au format YYYY-MM-DD
    datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    # Récupération des données
    c.execute('SELECT Article_resultat FROM Article_final WHERE date = %s', (datetime_Monitoring,))
    resultat = c.fetchone()

    # Fermeture de la connexion
    c.close()
    conn.close()

    if resultat:
        MESSAGE = resultat[0]  # Assurez-vous d'extraire le texte du tuple
    else:
        MESSAGE = "Aucun résultat trouvé pour la date:" + datetime_Monitoring
        print(MESSAGE)

    # URL du webhook Discord
    WEBHOOK_URL = 'https://discord.com/api/webhooks/1215411943771217940/_9YSyetO1Ilc8sfBgngImVQTAcuubhyxBzZ6r1ax_qCisP-lfLu3uYXTMAY9C8BIcffU'

    # Chemin vers le fichier vidéo
    VIDEO_PATH = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/{datetime_Monitoring}_{Theme}_monitoring_.mp4"

    # Envoi de la requête POST au webhook avec le texte et la vidéo
    with open(VIDEO_PATH, 'rb') as f:
        files = {
            'file': (VIDEO_PATH.split('/')[-1], f),
        }
        data = {
            'content': MESSAGE
        }
        response = requests.post(WEBHOOK_URL, files=files, data=data)

    # Vérification de la réponse
    if response.status_code == 204:
        print("Message et vidéo envoyés avec succès!")
    else:
        print(f"Échec de l'envoi: {response.status_code} - {response.text}")

    pass