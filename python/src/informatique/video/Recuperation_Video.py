import os
import random
import sys
import requests
import shutil
from datetime import datetime, timedelta
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from setting import API_KEY, connect_db, Theme

datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

def recuperation_videos():
    URL = 'https://pixabay.com/api/videos/'
    print("recuperation_videos")

    def telecharger_videos(mot_cle, index):
        params = {
            'key': API_KEY,
            'q': mot_cle,
            'lang': 'en',
            'video_type': 'film',
            'orientation': 'horizontal',
            'category': '',
            'safesearch': 'true',
            'order': 'latest',
            'page': random.randint(1, 5),
            'per_page': 3,
        }
        response = requests.get(URL, params=params)
        if response.status_code == 200:
            data = response.json()
            videos_trouvees = data['hits']
            if len(videos_trouvees) > 0:
                for i, video in enumerate(videos_trouvees[:3]):  # Limite à 3 vidéos
                    video_url = video['videos']['medium']['url']
                    dossier_destination = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/"
                    nom_fichier = f'video_article_{index}_p{i+1}.mp4'
                    file_path = os.path.join(dossier_destination, nom_fichier)
                    if not os.path.exists(dossier_destination):
                        os.makedirs(dossier_destination)
                    with requests.get(video_url, stream=True) as r:
                        with open(file_path, 'wb') as f:
                            shutil.copyfileobj(r.raw, f)
                    print(f'Vidéo {i+1} sauvegardée sous :', file_path)
            else:
                print('Aucune vidéo trouvée pour ce thème. Tentative avec le mot-clé par défaut...')
                if mot_cle != 'MacBook':  # Évite la boucle infinie avec le mot-clé de secours
                    telecharger_videos('MacBook', index)
        else:
            print('Erreur lors de la requête:', response.status_code)

    conn = connect_db()
    c = conn.cursor()
    date_du_jour_avant = datetime_Monitoring

    c.execute('SELECT mots_clée_1, mots_clée_2, mots_clée_3, mots_clée_4, mots_clée_5 FROM Video_mots WHERE date = %s', (date_du_jour_avant,))
    resultat = c.fetchone()

    if resultat:
        for i, mot_cle in enumerate(resultat, start=1):
            if mot_cle:
                telecharger_videos(mot_cle, i)
    else:
        print("Aucun résultat trouvé pour la date d'hier.")
    conn.close()
    pass