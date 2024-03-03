import os
import random
import sys
import requests
import shutil
from datetime import datetime, timedelta
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from setting import API_KEY, connect_db



def recuperation_videos():

    # URL de l'API Pixabay
    URL = 'https://pixabay.com/api/videos/'

    # Fonction pour télécharger les vidéos
    def telecharger_videos(mot_cle, index):
        params = {
            'key': API_KEY,
            'q': f'{mot_cle}',  # Thème de recherche
            'lang': 'en',  # Langue de recherche
            'video_type': 'all',  # Rechercher tous types de vidéos
            'orientation': 'horizontal',  # Orientation des vidéos
            'video_type' : 'film',
            'category': '',  # Vous pouvez spécifier une catégorie ici si nécessaire
            'safesearch': 'true',  # Activer le filtrage de contenu approprié
            'order': 'latest',  # Trier par popularité
            'page': random.randint(1, 5),  # Numéro de la page de résultats (aléatoire)
            'per_page': 3,  # Nombre de résultats par page, ajusté pour récupérer une seule vidéo
        }
        response = requests.get(URL, params=params)

        if response.status_code == 200:
            data = response.json()
            total_videos = len(data['hits'])  # Nombre total de vidéos retournées
            if total_videos > 0:
                for i in range(total_videos):
                    video_url = data['hits'][i]['videos']['medium']['url']
                    dossier_destination = f"./python/data/veille_video/veille_du_{date_du_jour_avant}/"
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
                if mot_cle == 'MacBook':
                    print('Impossible de trouver des vidéos avec le mot-clé par défaut.')
                else:
                    telecharger_videos('MacBook', index)  # Utilisation du mot-clé par défaut
        else:
            print('Erreur lors de la requête:', response.status_code)


    # Connexion à la base de données
    conn = connect_db()
    c = conn.cursor()
    date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    # Exécution de la requête pour récupérer les mots clés datés d'hier
    c.execute('SELECT mots_clée_1, mots_clée_2, mots_clée_3, mots_clée_4, mots_clée_5 FROM Video_mots WHERE date = %s', (date_du_jour_avant,))
    resultat = c.fetchone()

    if resultat:
        mots_cles = resultat
        print("Recup")
        for i, mot_cle in enumerate(mots_cles, start=1):
            if mot_cle:
                telecharger_videos(mot_cle, i)
    else:
        print("Aucun résultat trouvé pour la date d'hier.")

    # Fermeture de la connexion à la base de données
    conn.close()