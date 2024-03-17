import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import random
from datetime import datetime, timedelta
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, concatenate_audioclips
from setting import Theme
import random
from moviepy.editor import VideoFileClip, AudioFileClip


datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

def ajustement_rush():
    print("ajustement_rush")
    datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    # Construire le chemin vers le répertoire
    directory_path = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/"

    # Initialiser la variable pour compter les fichiers
    nombre_de_fichiers1 = 0

    # Vérifier si le répertoire existe pour éviter une erreur
    if os.path.exists(directory_path):
        for filename in os.listdir(directory_path):
            if filename.startswith("video_article_1_p"):
                nombre_de_fichiers1 += 1

        # Initialiser la variable pour compter les fichiers
    nombre_de_fichiers2 = 0

    # Vérifier si le répertoire existe pour éviter une erreur
    if os.path.exists(directory_path):
        for filename in os.listdir(directory_path):
            if filename.startswith("video_article_2_p"):
                nombre_de_fichiers2 += 1
    
        # Initialiser la variable pour compter les fichiers
    nombre_de_fichiers3 = 0

    # Vérifier si le répertoire existe pour éviter une erreur
    if os.path.exists(directory_path):
        for filename in os.listdir(directory_path):
            if filename.startswith("video_article_3_p"):
                nombre_de_fichiers3 += 1
    
        # Initialiser la variable pour compter les fichiers
    nombre_de_fichiers4 = 0

    # Vérifier si le répertoire existe pour éviter une erreur
    if os.path.exists(directory_path):
        for filename in os.listdir(directory_path):
            if filename.startswith("video_article_4_p"):
                nombre_de_fichiers4 += 1
    
        # Initialiser la variable pour compter les fichiers
    nombre_de_fichiers5 = 0

    # Vérifier si le répertoire existe pour éviter une erreur
    if os.path.exists(directory_path):
        for filename in os.listdir(directory_path):
            if filename.startswith("video_article_5_p"):
                nombre_de_fichiers5 += 1


    datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    nombre_aleatoire_entier = random.randint(1, 2)
    nombre_aleatoire_entier

    date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')




    chemin_video = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/video_article_1_p{nombre_de_fichiers1}.mp4"
    chemin_audio = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/audio_article_1.mp3"

    # Chargement des clips
    clip_video = VideoFileClip(chemin_video)
    clip_audio = AudioFileClip(chemin_audio)

    # Obtention des durées
    duree_video = clip_video.duration
    duree_audio = clip_audio.duration

    # Ajustement de la durée du clip vidéo pour correspondre à celle de l'audio
    if duree_video > duree_audio:
        # Coupe le clip vidéo si la vidéo est plus longue que l'audio
        clip_video_ajuste = clip_video.subclip(0, duree_audio)
    elif duree_video < duree_audio:
        # Boucle la vidéo si la vidéo est plus courte que l'audio
        # Assurez-vous de ne pas dépasser la durée de l'audio lors du bouclage
        repetition = duree_audio // duree_video  # Nombre entier de répétitions
        reste = duree_audio % duree_video  # Durée restante après les répétitions entières
        clip_repete = clip_video.loop(n=repetition)
        clip_reste = clip_video.subclip(0, reste)
        clip_video_ajuste = concatenate_videoclips([clip_repete, clip_reste])
    else:
        # La vidéo et l'audio ont déjà la même durée
        clip_video_ajuste = clip_video

    # Sauvegarde du clip vidéo ajusté
    clip_video_ajuste.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/Acticle_1_finale.mp4")












    chemin_video = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/video_article_2_p{nombre_de_fichiers2}.mp4"
    chemin_audio = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/audio_article_2.mp3"

    # Chargement des clips
    clip_video = VideoFileClip(chemin_video)
    clip_audio = AudioFileClip(chemin_audio)

    # Obtention des durées
    duree_video = clip_video.duration
    duree_audio = clip_audio.duration

    # Ajustement de la durée du clip vidéo pour correspondre à celle de l'audio
    if duree_video > duree_audio:
        # Coupe le clip vidéo si la vidéo est plus longue que l'audio
        clip_video_ajuste = clip_video.subclip(0, duree_audio)
    elif duree_video < duree_audio:
        # Boucle la vidéo si la vidéo est plus courte que l'audio
        # Assurez-vous de ne pas dépasser la durée de l'audio lors du bouclage
        repetition = duree_audio // duree_video  # Nombre entier de répétitions
        reste = duree_audio % duree_video  # Durée restante après les répétitions entières
        clip_repete = clip_video.loop(n=repetition)
        clip_reste = clip_video.subclip(0, reste)
        clip_video_ajuste = concatenate_videoclips([clip_repete, clip_reste])
    else:
        # La vidéo et l'audio ont déjà la même durée
        clip_video_ajuste = clip_video

    # Sauvegarde du clip vidéo ajusté
    clip_video_ajuste.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/Acticle_2_finale.mp4")


    chemin_video = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/video_article_3_p{nombre_de_fichiers3}.mp4"
    chemin_audio = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/audio_article_3.mp3"

    # Chargement des clips
    clip_video = VideoFileClip(chemin_video)
    clip_audio = AudioFileClip(chemin_audio)

    # Obtention des durées
    duree_video = clip_video.duration
    duree_audio = clip_audio.duration

    # Ajustement de la durée du clip vidéo pour correspondre à celle de l'audio
    if duree_video > duree_audio:
        # Coupe le clip vidéo si la vidéo est plus longue que l'audio
        clip_video_ajuste = clip_video.subclip(0, duree_audio)
    elif duree_video < duree_audio:
        # Boucle la vidéo si la vidéo est plus courte que l'audio (optionnel, selon votre besoin)
        clip_video_ajuste = clip_video.loop(duration=duree_audio)
    else:
        # La vidéo et l'audio ont déjà la même durée
        clip_video_ajuste = clip_video

    # Sauvegarde du clip vidéo ajusté
    clip_video_ajuste.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/Acticle_3_finale.mp4")





    chemin_video = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/video_article_4_p{nombre_de_fichiers4}.mp4"
    chemin_audio = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/audio_article_4.mp3"

    # Chargement des clips
    clip_video = VideoFileClip(chemin_video)
    clip_audio = AudioFileClip(chemin_audio)

    # Obtention des durées
    duree_video = clip_video.duration
    duree_audio = clip_audio.duration

    # Ajustement de la durée du clip vidéo pour correspondre à celle de l'audio
    if duree_video > duree_audio:
        # Coupe le clip vidéo si la vidéo est plus longue que l'audio
        clip_video_ajuste = clip_video.subclip(0, duree_audio)
    elif duree_video < duree_audio:
        # Boucle la vidéo si la vidéo est plus courte que l'audio
        # Assurez-vous de ne pas dépasser la durée de l'audio lors du bouclage
        repetition = duree_audio // duree_video  # Nombre entier de répétitions
        reste = duree_audio % duree_video  # Durée restante après les répétitions entières
        clip_repete = clip_video.loop(n=repetition)
        clip_reste = clip_video.subclip(0, reste)
        clip_video_ajuste = concatenate_videoclips([clip_repete, clip_reste])
    else:
        # La vidéo et l'audio ont déjà la même durée
        clip_video_ajuste = clip_video

    # Sauvegarde du clip vidéo ajusté
    clip_video_ajuste.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/Acticle_4_finale.mp4")

    chemin_video = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/video_article_5_p{nombre_de_fichiers5}.mp4"
    chemin_audio = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/audio_article_5.mp3"

    # Chargement des clips
    clip_video = VideoFileClip(chemin_video)
    clip_audio = AudioFileClip(chemin_audio)

    # Obtention des durées
    duree_video = clip_video.duration
    duree_audio = clip_audio.duration

    # Ajustement de la durée du clip vidéo pour correspondre à celle de l'audio
    if duree_video > duree_audio:
        # Coupe le clip vidéo si la vidéo est plus longue que l'audio
        clip_video_ajuste = clip_video.subclip(0, duree_audio)
    elif duree_video < duree_audio:
        # Boucle la vidéo si la vidéo est plus courte que l'audio (optionnel, selon votre besoin)
        clip_video_ajuste = clip_video.loop(duration=duree_audio)
    else:
        # La vidéo et l'audio ont déjà la même durée
        clip_video_ajuste = clip_video

    # Sauvegarde du clip vidéo ajusté
    clip_video_ajuste.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/Acticle_5_finale.mp4")















    # Configuration initiale
    chemin_repertoire = "./python/data/Ressource/"
    chemin_audio = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/intro.mp3"

    # Sélection d'une vidéo aléatoire
    fichiers = os.listdir(chemin_repertoire)
    extensions_videos = ('.mp4', '.avi', '.mov', '.mkv')
    videos = [fichier for fichier in fichiers if fichier.endswith(extensions_videos)]
    video_aleatoire = random.choice(videos) if videos else None

    if video_aleatoire:
        chemin_video = os.path.join(chemin_repertoire, video_aleatoire)
        print(f"Vidéo sélectionnée aléatoirement : {chemin_video}")
        
        # Chargement des clips
        clip_video = VideoFileClip(chemin_video)
        clip_audio = AudioFileClip(chemin_audio)
        
        # Obtention des durées
        duree_video = clip_video.duration
        duree_audio = clip_audio.duration
        
        # Ajustement de la vidéo
        if duree_video >= duree_audio:
            debut_aleatoire = random.uniform(0, duree_video - duree_audio)
            clip_video_ajuste = clip_video.subclip(debut_aleatoire, debut_aleatoire + duree_audio)
        else:
            # Optionnel : boucler la vidéo si plus courte que l'audio, puis couper
            clip_video_boucle = clip_video.loop(duration=duree_audio)
            debut_aleatoire = random.uniform(0, clip_video_boucle.duration - duree_audio)
            clip_video_ajuste = clip_video_boucle.subclip(debut_aleatoire, debut_aleatoire + duree_audio)
        
        # Sauvegarde du clip vidéo ajusté
        chemin_sortie = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/intro_finale.mp4"
        clip_video_ajuste.write_videofile(chemin_sortie)
    else:
        print("Aucune vidéo trouvée dans le répertoire spécifié.")





    # Configuration initiale
    chemin_repertoire = "./python/data/Ressource/"
    chemin_audio = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/outro.mp3"

    # Sélection d'une vidéo aléatoire
    fichiers = os.listdir(chemin_repertoire)
    extensions_videos = ('.mp4', '.avi', '.mov', '.mkv')
    videos = [fichier for fichier in fichiers if fichier.endswith(extensions_videos)]
    video_aleatoire = random.choice(videos) if videos else None

    if video_aleatoire:
        chemin_video = os.path.join(chemin_repertoire, video_aleatoire)
        print(f"Vidéo sélectionnée aléatoirement : {chemin_video}")
        
        # Chargement des clips
        clip_video = VideoFileClip(chemin_video)
        clip_audio = AudioFileClip(chemin_audio)
        
        # Obtention des durées
        duree_video = clip_video.duration
        duree_audio = clip_audio.duration
        
        # Ajustement de la vidéo
        if duree_video >= duree_audio:
            debut_aleatoire = random.uniform(0, duree_video - duree_audio)
            clip_video_ajuste = clip_video.subclip(debut_aleatoire, debut_aleatoire + duree_audio)
        else:
            # Optionnel : boucler la vidéo si plus courte que l'audio, puis couper
            clip_video_boucle = clip_video.loop(duration=duree_audio)
            debut_aleatoire = random.uniform(0, clip_video_boucle.duration - duree_audio)
            clip_video_ajuste = clip_video_boucle.subclip(debut_aleatoire, debut_aleatoire + duree_audio)
        
        # Sauvegarde du clip vidéo ajusté
        chemin_sortie =f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/outro_finale.mp4"
        clip_video_ajuste.write_videofile(chemin_sortie)
    else:
        print("Aucune vidéo trouvée dans le répertoire spécifié.")
    pass





