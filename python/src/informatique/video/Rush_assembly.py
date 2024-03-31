import sys
from pathlib import Path
from datetime import datetime, timedelta
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, concatenate_audioclips, ImageClip, CompositeVideoClip

sys.path.append(str(Path(__file__).parent.parent))
from Setting.setting import  Theme

datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

def ajuster_format_telephone(clip, resolution_cible=(1080, 1920)):
    ratio_cible = resolution_cible[0] / resolution_cible[1]
    ratio_clip = clip.size[0] / clip.size[1]

    if ratio_clip > ratio_cible:
        # Le clip est trop large, il faut le rogner horizontalement
        nouvelle_largeur = int(clip.size[1] * ratio_cible)
        clip_rogne = clip.crop(x_center=clip.size[0]/2, width=nouvelle_largeur)
    else:
        # Le clip est trop haut, il faut le rogner verticalement (si nécessaire)
        nouvelle_hauteur = int(clip.size[0] / ratio_cible)
        clip_rogne = clip.crop(y_center=clip.size[1]/2, height=nouvelle_hauteur)

    # Redimensionnement pour s'assurer que la résolution correspond à la cible
    clip_final = clip_rogne.resize(newsize=resolution_cible)
    return clip_final

def rush_assembly():
    try:
        print("-")
        print("🟦 Rush assembly [ B{8/10} ]🟦")
        target_fps = 24
        codec_video = 'libx264'
        resolution = (1080, 1920)

        base_path = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}"
        video_intro_path = f"{base_path}/final_component/intro_finale.mp4"
        video_outro_path = f"{base_path}/final_component/outro_finale.mp4"
        base_pathv = f"{base_path}/final_component/"
        base_patha = f"{base_path}/audio/"

        # Traitement de l'intro et de l'outro
        video_intro_clip = VideoFileClip(video_intro_path)
        video_intro_ajuste = ajuster_format_telephone(video_intro_clip, resolution)
        video_outro_clip = VideoFileClip(video_outro_path)
        video_outro_ajuste = ajuster_format_telephone(video_outro_clip, resolution)

        video_clips = []
        audio_clips = [AudioFileClip(f"{base_patha}/intro.mp3")]

        for i in range(1, 6):
            source_filename = f"{base_pathv}/Acticle_{i}_finale.mp4"
            destination_filename = f"{base_pathv}/Acticle_{i}_finale_prepare.mp4"
            
            clip = VideoFileClip(source_filename)
            clip_ajuste = ajuster_format_telephone(clip, resolution)
            clip_ajuste.write_videofile(destination_filename, codec=codec_video)
            video_clips.append(VideoFileClip(destination_filename))  

            audio_clips.append(AudioFileClip(f"{base_patha}/audio_article_{i}.mp3"))

        audio_clips.append(AudioFileClip(f"{base_patha}/outro.mp3"))

        clip_final = concatenate_videoclips([video_intro_ajuste] + video_clips + [video_outro_ajuste])
        clip_audio_final = concatenate_audioclips(audio_clips)
        clip_final = clip_final.set_audio(clip_audio_final)

        nom_fichier_sortie_video = f"{base_pathv}/assembly.mp4"
        clip_final.write_videofile(nom_fichier_sortie_video, codec=codec_video)

        image_path = '/Applications/XAMPP/xamppfiles/htdocs/DATA-NEST-V2/python/data/Ressource/back.png'  # Chemin vers votre image
        image_clip = ImageClip(image_path).set_duration(clip_final.duration).resize(resolution)
        final_video_with_image = CompositeVideoClip([clip_final, image_clip])
        
        nom_fichier_sortie_video = f"{base_pathv}/assembly.mp4"
        final_video_with_image.write_videofile(nom_fichier_sortie_video, codec=codec_video)
        

        nom_fichier_sortie_audio = f"{base_patha}/Compilation_audio_finale.mp3"
        clip_audio_final.write_audiofile(nom_fichier_sortie_audio)

        video_intro_clip.close()
        video_outro_clip.close()
        for clip in video_clips + audio_clips:
            clip.close()

    except Exception as e:
            print(f"""❌❌An error has occurred(Rush assembly) ❌❌
            ➡️Here is the error message 🟨{e}🟨 """)
