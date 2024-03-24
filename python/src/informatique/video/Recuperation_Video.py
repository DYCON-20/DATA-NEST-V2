import os
import random
import requests
import shutil
from datetime import datetime, timedelta
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from Setting.setting import  API_KEY, connect_db, Theme

datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

def recuperation_videos():
    
    print("-")
    print("🟦 Thanks to the keyword recover the videos [ B{5/10} ]🟦")

    URL = 'https://pixabay.com/api/videos/'
    
    # Définition d'une liste de mots-clés de secours
    mots_cles_secours = ['MacBook', 'technology', 'city', 'education', 'music']

    def telecharger_video(url, dossier_destination, nom_fichier):
        if not os.path.exists(dossier_destination):
            os.makedirs(dossier_destination)
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(os.path.join(dossier_destination, nom_fichier), 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print(f'⬜️ Video saved as: : {nom_fichier} ⬜️')

    def trouver_et_telecharger_videos(mot_cle, index, nombre_videos=3):
        videos_trouvees = 0
        page = random.randint(1, 5)
        while videos_trouvees < nombre_videos:
            params = {
                'key': API_KEY,
                'q': mot_cle,
                'lang': 'en',
                'video_type': 'film',
                'orientation': 'horizontal',
                'category': '',
                'safesearch': 'true',
                'order': 'latest',
                'page': page,
                'per_page': nombre_videos - videos_trouvees,
            }
            response = requests.get(URL, params=params)
            if response.status_code == 200:
                data = response.json()
                for video in data['hits']:
                    video_url = video['videos']['medium']['url']
                    nom_fichier = f'video_article_{index}_p{videos_trouvees+1}.mp4'
                    dossier_destination = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/"
                    telecharger_video(video_url, dossier_destination, nom_fichier)
                    videos_trouvees += 1
                    if videos_trouvees >= nombre_videos:
                        break
            else:
                print(f'❌: {response.status_code}')
                break
            if videos_trouvees < nombre_videos:
                mot_cle = random.choice(mots_cles_secours)  # Sélection aléatoire d'un mot-clé de secours
                page = 1  

    conn = connect_db()
    c = conn.cursor()
    date_du_jour_avant = datetime_Monitoring

    c.execute('SELECT mots_clee_1, mots_clee_2, mots_clee_3, mots_clee_4, mots_clee_5 FROM Video_mots WHERE date = %s', (date_du_jour_avant,))
    resultat = c.fetchone()

    if resultat:
        for i, mot_cle in enumerate(resultat, start=1):
            if mot_cle:
                trouver_et_telecharger_videos(mot_cle, i)
    else:
        print("❌ No results found for yesterday's date ❌")
    conn.close()
    pass