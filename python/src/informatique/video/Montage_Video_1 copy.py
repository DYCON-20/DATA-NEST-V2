#rejouter fonction nom+date
#rajouter supresion rush 
import os
import pysrt
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import random
from datetime import datetime, timedelta
from mutagen.mp3 import MP3
from moviepy.editor import VideoFileClip, AudioFileClip
import requests
from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
from setting import AssemblyAI  # Assurez-vous que ce module contient la configuration nécessaire pour utiliser l'API AssemblyAI

from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, concatenate_audioclips
from setting import AssemblyAI
import assemblyai as aai

from setting import Theme


datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

def ajustement_rush():

    nombre_aleatoire_entier = random.randint(1, 2)
    nombre_aleatoire_entier

    date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    chemin_video = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/video_article_1_p{nombre_aleatoire_entier}.mp4"
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
        # Boucle la vidéo si la vidéo est plus courte que l'audio (optionnel, selon votre besoin)
        clip_video_ajuste = clip_video.loop(duration=duree_audio)
    else:
        # La vidéo et l'audio ont déjà la même durée
        clip_video_ajuste = clip_video

    # Sauvegarde du clip vidéo ajusté
    clip_video_ajuste.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/Acticle_1_finale.mp4")



    chemin_video = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/video_article_2_p{nombre_aleatoire_entier}.mp4"
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
        # Boucle la vidéo si la vidéo est plus courte que l'audio (optionnel, selon votre besoin)
        clip_video_ajuste = clip_video.loop(duration=duree_audio)
    else:
        # La vidéo et l'audio ont déjà la même durée
        clip_video_ajuste = clip_video

    # Sauvegarde du clip vidéo ajusté
    clip_video_ajuste.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/Acticle_2_finale.mp4")


    chemin_video = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/video_article_3_p{nombre_aleatoire_entier}.mp4"
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

    chemin_video = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/video_article_4_p{nombre_aleatoire_entier}.mp4"
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
        # Boucle la vidéo si la vidéo est plus courte que l'audio (optionnel, selon votre besoin)
        clip_video_ajuste = clip_video.loop(duration=duree_audio)
    else:
        # La vidéo et l'audio ont déjà la même durée
        clip_video_ajuste = clip_video

    # Sauvegarde du clip vidéo ajusté
    clip_video_ajuste.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/Acticle_4_finale.mp4")

    chemin_video = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/video_article_5_p{nombre_aleatoire_entier}.mp4"
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
