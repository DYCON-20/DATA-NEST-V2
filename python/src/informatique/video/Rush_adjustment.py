import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import random
from datetime import datetime, timedelta
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, concatenate_audioclips
from Setting.setting import  Theme
import random
from moviepy.editor import VideoFileClip, AudioFileClip

datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

def rush_adjustment():
    try:
        print("-")
        print("Creating the video filter [4/i]")
        datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

     
        directory_path = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/"

     
        nombre_de_fichiers1 = 0

     
        if os.path.exists(directory_path):
            for filename in os.listdir(directory_path):
                if filename.startswith("video_article_1_p"):
                    nombre_de_fichiers1 += 1

         
        nombre_de_fichiers2 = 0

     
        if os.path.exists(directory_path):
            for filename in os.listdir(directory_path):
                if filename.startswith("video_article_2_p"):
                    nombre_de_fichiers2 += 1
        
         
        nombre_de_fichiers3 = 0

     
        if os.path.exists(directory_path):
            for filename in os.listdir(directory_path):
                if filename.startswith("video_article_3_p"):
                    nombre_de_fichiers3 += 1
        
         
        nombre_de_fichiers4 = 0

     
        if os.path.exists(directory_path):
            for filename in os.listdir(directory_path):
                if filename.startswith("video_article_4_p"):
                    nombre_de_fichiers4 += 1
        
         
        nombre_de_fichiers5 = 0

     
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

     
        clip_video = VideoFileClip(chemin_video)
        clip_audio = AudioFileClip(chemin_audio)

     
        duree_video = clip_video.duration
        duree_audio = clip_audio.duration

     
        if duree_video > duree_audio:
     
            clip_video_ajuste = clip_video.subclip(0, duree_audio)
        elif duree_video < duree_audio:
     
            clip_video_ajuste = clip_video.loop(duration=duree_audio)
        else:
     
            clip_video_ajuste = clip_video

     
        clip_video_ajuste = clip_video_ajuste.set_audio(clip_audio)
        

     
        clip_video_ajuste.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/Acticle_1_finale.mp4")












        chemin_video = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/video_article_2_p{nombre_de_fichiers2}.mp4"
        chemin_audio = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/audio_article_2.mp3"

     
        clip_video = VideoFileClip(chemin_video)
        clip_audio = AudioFileClip(chemin_audio)

     
        duree_video = clip_video.duration
        duree_audio = clip_audio.duration

     
        if duree_video > duree_audio:
     
            clip_video_ajuste = clip_video.subclip(0, duree_audio)
        elif duree_video < duree_audio:
     
            clip_video_ajuste = clip_video.loop(duration=duree_audio)
        else:
     
            clip_video_ajuste = clip_video

     
        clip_video_ajuste = clip_video_ajuste.set_audio(clip_audio)
        

     
        clip_video_ajuste.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/Acticle_2_finale.mp4")


        chemin_video = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/video_article_3_p{nombre_de_fichiers3}.mp4"
        chemin_audio = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/audio_article_3.mp3"

     
        clip_video = VideoFileClip(chemin_video)
        clip_audio = AudioFileClip(chemin_audio)

     
        duree_video = clip_video.duration
        duree_audio = clip_audio.duration

     
        if duree_video > duree_audio:
     
            clip_video_ajuste = clip_video.subclip(0, duree_audio)
        elif duree_video < duree_audio:
     
            clip_video_ajuste = clip_video.loop(duration=duree_audio)
        else:
     
            clip_video_ajuste = clip_video

     
        clip_video_ajuste = clip_video_ajuste.set_audio(clip_audio)
        
        clip_video_ajuste.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/Acticle_3_finale.mp4")





        chemin_video = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/video_article_4_p{nombre_de_fichiers4}.mp4"
        chemin_audio = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/audio_article_4.mp3"

     
        clip_video = VideoFileClip(chemin_video)
        clip_audio = AudioFileClip(chemin_audio)

     
        duree_video = clip_video.duration
        duree_audio = clip_audio.duration

     
        if duree_video > duree_audio:
     
            clip_video_ajuste = clip_video.subclip(0, duree_audio)
        elif duree_video < duree_audio:
     
            clip_video_ajuste = clip_video.loop(duration=duree_audio)
        else:
     
            clip_video_ajuste = clip_video

     
        clip_video_ajuste = clip_video_ajuste.set_audio(clip_audio)
     
        clip_video_ajuste.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/Acticle_4_finale.mp4")








        chemin_video = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video/video_article_5_p{nombre_de_fichiers5}.mp4"
        chemin_audio = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/audio_article_5.mp3"

     
        clip_video = VideoFileClip(chemin_video)
        clip_audio = AudioFileClip(chemin_audio)

     
        duree_video = clip_video.duration
        duree_audio = clip_audio.duration

     
        if duree_video > duree_audio:
     
            clip_video_ajuste = clip_video.subclip(0, duree_audio)
        elif duree_video < duree_audio:
     
            clip_video_ajuste = clip_video.loop(duration=duree_audio)
        else:
     
            clip_video_ajuste = clip_video

     
        clip_video_ajuste = clip_video_ajuste.set_audio(clip_audio)
     
        clip_video_ajuste.write_videofile(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/Acticle_5_finale.mp4")















     
        chemin_repertoire = "./python/data/Ressource/"
        chemin_audio = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/intro.mp3"

     
        fichiers = os.listdir(chemin_repertoire)
        extensions_videos = ('.mp4', '.avi', '.mov', '.mkv')
        videos = [fichier for fichier in fichiers if fichier.endswith(extensions_videos)]
        video_aleatoire = random.choice(videos) if videos else None

        if video_aleatoire:
            chemin_video = os.path.join(chemin_repertoire, video_aleatoire)
            print(f"Vidéo sélectionnée aléatoirement : {chemin_video}")
            
             
            clip_video = VideoFileClip(chemin_video)
            clip_audio = AudioFileClip(chemin_audio)

         
            duree_video = clip_video.duration
            duree_audio = clip_audio.duration

         
            if duree_video > duree_audio:
         
                clip_video_ajuste = clip_video.subclip(0, duree_audio)
            elif duree_video < duree_audio:
         
                clip_video_ajuste = clip_video.loop(duration=duree_audio)
            else:
         
                clip_video_ajuste = clip_video

         
            clip_video_ajuste = clip_video_ajuste.set_audio(clip_audio)
         
            chemin_sortie = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/intro_finale.mp4"
            clip_video_ajuste.write_videofile(chemin_sortie)
        else:
            print("Aucune vidéo trouvée dans le répertoire spécifié.")





     
        chemin_repertoire = "./python/data/Ressource/"
        chemin_audio = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/outro.mp3"

     
        fichiers = os.listdir(chemin_repertoire)
        extensions_videos = ('.mp4', '.avi', '.mov', '.mkv')
        videos = [fichier for fichier in fichiers if fichier.endswith(extensions_videos)]
        video_aleatoire = random.choice(videos) if videos else None

        if video_aleatoire:
         
            clip_video = VideoFileClip(chemin_video)
            clip_audio = AudioFileClip(chemin_audio)

         
            duree_video = clip_video.duration
            duree_audio = clip_audio.duration

         
            if duree_video > duree_audio:
         
                clip_video_ajuste = clip_video.subclip(0, duree_audio)
            elif duree_video < duree_audio:
         
                clip_video_ajuste = clip_video.loop(duration=duree_audio)
            else:
         
                clip_video_ajuste = clip_video

         
            clip_video_ajuste = clip_video_ajuste.set_audio(clip_audio)
         
            chemin_sortie =f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/outro_finale.mp4"
            clip_video_ajuste.write_videofile(chemin_sortie)
        else:
            print("Aucune vidéo trouvée dans le répertoire spécifié.")
        pass

    except Exception as e:
            print(f"""❌❌An error has occurred(Creating the video filter) ❌❌
            ➡️Here is the error message 🟨{e}🟨 """)

