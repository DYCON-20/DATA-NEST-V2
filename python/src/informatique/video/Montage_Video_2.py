import os
import sys
from pathlib import Path
from datetime import datetime, timedelta
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, concatenate_audioclips
from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx
# Ajout du chemin du projet pour importer des modules spécifiques
sys.path.append(str(Path(__file__).parent.parent))
from setting import Theme


datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
def assamblage_rush():
    # Génération de la date du jour précédent
    date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')




    # Paramètres de la vidéo cible ajustés pour format téléphone
    target_fps = 24
    codec_video = 'libx264'
    resolution = (720, 1280)  # Résolution ajustée pour le format portrait

    for i in range(1, 6):
        source_filename = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/Acticle_{i}_finale.mp4"
        destination_filename = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/Acticle_{i}_finale_prepare.mp4"
        
        clip = VideoFileClip(source_filename)

        # Calcul pour centrer et rogner l'image pour le format portrait
        clip_cropped = clip.crop(x_center=clip.size[0]/2, y_center=clip.size[1]/2, width=min(clip.size[0], resolution[0]), height=min(clip.size[1], resolution[1]))
        
        # Ajustement de la résolution et des fps après rognage
        clip_resized = clip_cropped.resize(newsize=resolution).set_fps(target_fps)
        
        clip_resized.write_videofile(destination_filename, codec=codec_video)

    # Préparation des chemins pour les clips vidéo et audio
    base_pathv = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/"
    base_patha = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/"
    base_pathf = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component/"

    video_clips = [f"Acticle_{i}_finale_prepare.mp4" for i in range(1, 6)]
    audio_clips = [f"audio_article_{i}.mp3" for i in range(1, 6)]

    # Chargement et fusion des clips vidéo
    video_clips_obj = [VideoFileClip(base_pathv + clip) for clip in video_clips]
    clip_final = concatenate_videoclips(video_clips_obj)
    
    # Chargement et fusion des clips audio
    audio_clips_obj = [AudioFileClip(base_patha + clip) for clip in audio_clips]
    clip_audio_final = concatenate_audioclips(audio_clips_obj)

    # Association de l'audio avec le clip vidéo
    clip_final = clip_final.set_audio(clip_audio_final)

    # Nom du fichier de sortie avec date et heure
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nom_fichier_sortie = f"{base_pathf}assembly.mp4"

    # Exportation du fichier final
    clip_final.write_videofile(nom_fichier_sortie)

    # Fermeture des clips pour libérer la mémoire
    for clip in video_clips_obj + audio_clips_obj:
        clip.close()


    audio1 = AudioFileClip(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/audio_article_1.mp3")
    audio2 = AudioFileClip(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/audio_article_2.mp3")
    audio3 = AudioFileClip(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/audio_article_3.mp3")
    audio4 = AudioFileClip(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio//audio_article_4.mp3")
    audio5 = AudioFileClip(f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/audio_article_5.mp3")
    # Fusion des clips audio dans l'ordre
    clip_audio_final = concatenate_audioclips([audio1, audio2, audio3, audio4, audio5])

    # Sauvegarde du clip audio final dans un fichier
    nom_fichier_sortie = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio/Compilation_audio_finale.mp3"
    clip_audio_final.write_audiofile(nom_fichier_sortie)