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





def assamblage_sous_titre_rush():



    nombre_aleatoire_entier = random.randint(1, 3)
    nombre_aleatoire_entier

    date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')



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
