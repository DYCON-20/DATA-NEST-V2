import os
import requests
import shutil
#from Chat_GPT_mots import mots_clée

# Remplacez 'VotreCleAPI' par votre clé API réelle de Pixabay
API_KEY = '42564024-9a8c511341d7fd5ac07b886bd'
URL = 'https://pixabay.com/api/videos/'

mots_clée_T = 'informatique'


# Paramètres de recherche pour les vidéos
params = {
    'key': API_KEY,
    'q': mots_clée_T,  # Thème de recherche
    'lang': 'fr',  # Langue de recherche
    'per_page': 5,  # Nombre de résultats par page
    'video_type': 'all',  # Rechercher tous types de vidéos
    'orientation': 'all',  # Pas de restriction sur l'orientation
    'category': 'science',  # Catégorie spécifique
    'max_width': 1920,  # Largeur minimale en pixels
    'max_height': 1080,  # Hauteur minimale en pixels
    'editors_choice': True,  # Uniquement les choix des éditeurs
    'safesearch': True,  # Exclure les contenus explicites
    'order': 'popular',  # Trier par popularité
    'page': 1,  # Numéro de la page de résultats
}
print(params)
response = requests.get(URL, params=params)

# Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()
    total_videos = len(data['hits'])  # Nombre total de vidéos retournées
    if total_videos > 0:
        for i in range(total_videos):
            # Prendre l'URL de chaque vidéo de la liste
            video_url = data['hits'][i]['videos']['medium']['url']
            
            # Chemin du dossier où les vidéos seront sauvegardées
            dossier_destination = 'python/src/informatique/Video_traitement'
            
            # Nom du fichier où chaque vidéo sera sauvegardée
            nom_fichier = f'video_informatique_{i+1}.mp4'
            file_path = os.path.join(dossier_destination, nom_fichier)
            
            # Vérifier si le dossier existe, sinon le créer
            if not os.path.exists(dossier_destination):
                os.makedirs(dossier_destination)
            
            # Téléchargement et sauvegarde de chaque vidéo
            with requests.get(video_url, stream=True) as r:
                with open(file_path, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
            
            print(f'Vidéo {i+1} sauvegardée sous :', file_path)
    else:
        print('Aucune vidéo trouvée pour ce thème.')
else:
    print('Erreur lors de la requête:', response.status_code)


