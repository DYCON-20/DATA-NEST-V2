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

nombre_aleatoire_entier = random.randint(1, 3)
nombre_aleatoire_entier

date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')





chemin_video = f"./python/data/veille_video/veille_du_{date_du_jour_avant}/video_article_1_p{nombre_aleatoire_entier}.mp4"
chemin_audio = f"./python/data/veille_video/veille_du_{date_du_jour_avant}/audio_article_1.mp3"

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
clip_video_ajuste.write_videofile(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/Acticle_1_finale.mp4")



chemin_video = f"./python/data/veille_video/veille_du_{date_du_jour_avant}/video_article_2_p{nombre_aleatoire_entier}.mp4"
chemin_audio = f"./python/data/veille_video/veille_du_{date_du_jour_avant}/audio_article_2.mp3"

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
clip_video_ajuste.write_videofile(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/Acticle_2_finale.mp4")


chemin_video = f"./python/data/veille_video/veille_du_{date_du_jour_avant}/video_article_3_p{nombre_aleatoire_entier}.mp4"
chemin_audio = f"./python/data/veille_video/veille_du_{date_du_jour_avant}/audio_article_3.mp3"

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
clip_video_ajuste.write_videofile(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/Acticle_3_finale.mp4")

chemin_video = f"./python/data/veille_video/veille_du_{date_du_jour_avant}/video_article_4_p{nombre_aleatoire_entier}.mp4"
chemin_audio = f"./python/data/veille_video/veille_du_{date_du_jour_avant}/audio_article_4.mp3"

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
clip_video_ajuste.write_videofile(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/Acticle_4_finale.mp4")


chemin_video = f"./python/data/veille_video/veille_du_{date_du_jour_avant}/video_article_5_p{nombre_aleatoire_entier}.mp4"
chemin_audio = f"./python/data/veille_video/veille_du_{date_du_jour_avant}/audio_article_5.mp3"

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
clip_video_ajuste.write_videofile(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/Acticle_5_finale.mp4")


clip1 = VideoFileClip(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/Acticle_1_finale.mp4")
clip2 = VideoFileClip(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/Acticle_2_finale.mp4")
clip3 = VideoFileClip(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/Acticle_3_finale.mp4")
clip4 = VideoFileClip(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/Acticle_4_finale.mp4")
clip5 = VideoFileClip(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/Acticle_5_finale.mp4")

# Chargement des clips audio
audio1 = AudioFileClip(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/audio_article_1.mp3")
audio2 = AudioFileClip(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/audio_article_2.mp3")
audio3 = AudioFileClip(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/audio_article_3.mp3")
audio4 = AudioFileClip(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/audio_article_4.mp3")
audio5 = AudioFileClip(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/audio_article_5.mp3")

# Fusion des clips audio dans l'ordre
clip_audio_final = concatenate_audioclips([audio1, audio2, audio3, audio4, audio5])

# Sauvegarde du clip audio final dans un fichier
nom_fichier_sortie = f"./python/data/veille_video/veille_du_{date_du_jour_avant}/Compilation_audio_finale.mp3"
clip_audio_final.write_audiofile(nom_fichier_sortie)


clip_final = concatenate_videoclips([clip1, clip2, clip3, clip4, clip5])


clip_final.write_videofile(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/montage.mp4")













from moviepy.editor import VideoFileClip, AudioFileClip

video_clip = VideoFileClip(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/montage.mp4")
audio_clip = AudioFileClip(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/Compilation_audio_finale.mp3")

# Assurez-vous que la durée de l'audio correspond à celle de la vidéo
video_clip = video_clip.set_audio(audio_clip)

video_clip.write_videofile(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/ms.mp4")





aai.settings.api_key = AssemblyAI

audio_url = f"./python/data/veille_video/veille_du_{date_du_jour_avant}/Compilation_audio_finale.mp3"

# Configurer la transcription pour le français
config = aai.TranscriptionConfig(language_code="fr")

# Créer l'objet Transcriber avec la configuration spécifiée
transcriber = aai.Transcriber(config=config)

# Lancer la transcription
transcript = transcriber.transcribe(audio_url)

# Imprimer le texte transcrit

srt = transcript.export_subtitles_srt()

# Sauvegarder le fichier SRT localement
with open(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/transcription_fr.srt", "w") as f:
    f.write(srt)


# Charger les sous-titres à partir du fichier SRT
subtitles = pysrt.open(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/transcription_fr.srt")

# Exemple de structure après parsing
for sub in subtitles:
    start = sub.start.ordinal / 1000  # Convertir en secondes
    end = sub.end.ordinal / 1000  # Convertir en secondes
    text = sub.text
    print(start, end, text)



from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def create_subtitle_clip(subtitle, start_time, end_time, video_size):
    """Crée un clip de texte pour un sous-titre."""
    txt_clip = TextClip(subtitle, fontsize=24, color='white', font='Arial', align='center', size=video_size)
    txt_clip = txt_clip.set_start(start_time).set_duration(end_time - start_time).set_position('bottom')
    return txt_clip

# Charger la vidéo originale
video = VideoFileClip(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/ms.mp4")

# Charger les sous-titres SRT
subtitles = pysrt.open(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/transcription_fr.srt")

# Créer des clips de sous-titres
subtitles_clips = [
    create_subtitle_clip(sub.text, sub.start.ordinal / 1000, sub.end.ordinal / 1000, video.size)
    for sub in subtitles
]

# Combiner la vidéo avec les clips de sous-titres
final_video = CompositeVideoClip([video] + subtitles_clips)

# Exporter la vidéo avec les sous-titres intégrés
final_video.write_videofile(f"./python/data/veille_video/veille_du_{date_du_jour_avant}/last.mp4", codec="libx264", fps=video.fps)
