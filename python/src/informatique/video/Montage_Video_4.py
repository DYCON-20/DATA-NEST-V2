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



def assamblage_sous_titre_rush():





    # Charger les sous-titres à partir du fichier SRT
    subtitles = pysrt.open(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/subtitle/transcription_fr.srt")

    # Exemple de structure après parsing
    for sub in subtitles:
        start = sub.start.ordinal / 1000  # Convertir en secondes
        end = sub.end.ordinal / 1000  # Convertir en secondes
        text = sub.text
        print(start, end, text)



    def create_subtitle_clip(subtitle, start_time, end_time, video_size):
        """Crée un clip de texte pour un sous-titre avec une police d'écriture spécifique, un fond noir et un contour noir autour du texte."""
        # Définit la largeur maximale du texte pour qu'il s'adapte à l'écran du téléphone
        max_text_width = video_size[0] * 0.9  # Utilise 90% de la largeur de la vidéo comme largeur max du texte
        
        txt_clip = TextClip(subtitle, fontsize=55, color='white', font='Inter-Bold', align='center',
                            size=(max_text_width, None), method='caption', bg_color='black',
                            stroke_color='white', stroke_width=2)  # Augmente `stroke_width` pour un contour plus visible
        
        # Centre le texte horizontalement et le positionne en bas de la vidéo avec un fond noir
        txt_clip = txt_clip.set_start(start_time).set_duration(end_time - start_time).set_position(('center', 0.7), 'center')
        
        return txt_clip








    # Charger la vidéo originale
    video = VideoFileClip(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/audio_video_editing.mp4")

    # Charger les sous-titres SRT
    subtitles = pysrt.open(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/subtitle/transcription_fr.srt")

    # Créer des clips de sous-titres
    subtitles_clips = [
        create_subtitle_clip(sub.text, sub.start.ordinal / 1000, sub.end.ordinal / 1000, video.size)
        for sub in subtitles
    ]

    # Combiner la vidéo avec les clips de sous-titres
    final_video = CompositeVideoClip([video] + subtitles_clips)

    # Exporter la vidéo avec les sous-titres intégrés
    final_video.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/{datetime_Monitoring}_{Theme}_monitoring_.mp4", codec="libx264", fps=video.fps)
