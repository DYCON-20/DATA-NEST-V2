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
from Setting.setting import  AssemblyAI  

from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, concatenate_audioclips
from Setting.setting import  AssemblyAI
import assemblyai as aai
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

from Setting.setting import  Theme


datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')



def assembly_under_rush_title():
    try:

        print("-")
        print("🟦 Create the video subtitles [ B{10/10} ]🟦")





        subtitles = pysrt.open(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/subtitle/transcription_fr.srt")

        for sub in subtitles:
            start = sub.start.ordinal / 1000  
            end = sub.end.ordinal / 1000  
            text = sub.text
            print(start, end, text)



        def create_subtitle_clip(subtitle, start_time, end_time, video_size):
            """Crée un clip de texte pour un sous-titre avec une police d'écriture spécifique, un fond noir et un contour noir autour du texte."""
            max_text_width = video_size[0] * 0.9 
            txt_clip = TextClip(subtitle, fontsize=65, color='white', font='Inter-Bold', align='west',
                                size=(max_text_width, None), method='caption',
                                stroke_color='white', stroke_width=1)  
            left_margin = 50  

            txt_clip = txt_clip.set_start(start_time).set_duration(end_time - start_time).set_position(('left_margin', 0.6), 'left')
            
            return txt_clip





        from moviepy.editor import TextClip

        def create_subtitle_clip(subtitle, start_time, end_time, video_size):
            """Crée un clip de texte pour un sous-titre avec une police d'écriture spécifique, un fond noir et un contour noir autour du texte."""

            max_text_width = video_size[0] * 0.9  
            txt_clip = TextClip(subtitle, fontsize=65, color='white', font='Inter-Bold', align='West',
                                size=(max_text_width,None), method='caption',
                                stroke_color='white', stroke_width=1)


            left_margin = 50  
            bottom_margin = 500  
            text_position = (left_margin, video_size[1] - txt_clip.size[1] - bottom_margin)

            txt_clip = txt_clip.set_start(start_time).set_duration(end_time - start_time).set_position(text_position)

            return txt_clip





        video = VideoFileClip(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/audio_video_editing.mp4")

        subtitles = pysrt.open(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/subtitle/transcription_fr.srt")

        subtitles_clips = [
            create_subtitle_clip(sub.text, sub.start.ordinal / 1000, sub.end.ordinal / 1000, video.size)
            for sub in subtitles
        ]

        final_video = CompositeVideoClip([video] + subtitles_clips)

        final_video.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/video.mp4", codec="libx264", fps=video.fps)



        video = VideoFileClip(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/audio_video_editing.mp4")

        subtitles = pysrt.open(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/subtitle/transcription_fr.srt")

        subtitles_clips = [
            create_subtitle_clip(sub.text, sub.start.ordinal / 1000, sub.end.ordinal / 1000, video.size)
            for sub in subtitles
        ]

        final_video = CompositeVideoClip([video] + subtitles_clips)

        final_video.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/video.mp4", codec="libx264", fps=video.fps)





        video_clip = VideoFileClip(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/video.mp4")

        background_audio_clip = AudioFileClip("./python/data/Ressource/echo.mp3")    

        background_audio_clip = background_audio_clip.volumex(0.02)  
        background_audio_clip = background_audio_clip.set_duration(video_clip.duration)

        composite_audio_clip = CompositeAudioClip([video_clip.audio, background_audio_clip])

        video_clip.audio = composite_audio_clip

        video_clip.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/{datetime_Monitoring}_{Theme}_monitoring_.mp4")
    except Exception as e:
            print(f"""❌❌An error has occurred (Create the video subtitles) ❌❌
            ➡️Here is the error message 🟨{e}🟨 """)
