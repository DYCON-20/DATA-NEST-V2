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
from setting import AssemblyAI  

from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, concatenate_audioclips
from setting import AssemblyAI
import assemblyai as aai

from setting import Theme


datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')



def crated_subtitle():
    print("crated_subtitle")



    nombre_aleatoire_entier = random.randint(1, 3)
    nombre_aleatoire_entier

    date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')



    from moviepy.editor import VideoFileClip, AudioFileClip

    video_clip = VideoFileClip(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/assembly.mp4")
    audio_clip = AudioFileClip(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/Compilation_audio_finale.mp3")

    # Assurez-vous que la durée de l'audio correspond à celle de la vidéo
    video_clip = video_clip.set_audio(audio_clip)

    video_clip.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/audio_video_editing.mp4")





    aai.settings.api_key = AssemblyAI

    audio_url = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/Compilation_audio_finale.mp3"

    # Configurer la transcription pour le français
    config = aai.TranscriptionConfig(language_code="fr")

    # Créer l'objet Transcriber avec la configuration spécifiée
    transcriber = aai.Transcriber(config=config)

    # Lancer la transcription
    transcript = transcriber.transcribe(audio_url)

    # Imprimer le texte transcrit

    srt = transcript.export_subtitles_srt()

    # Sauvegarder le fichier SRT localement
    with open(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/subtitle/transcription_fr.srt", "w") as f:
        f.write(srt)

    pass
  