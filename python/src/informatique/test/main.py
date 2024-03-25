import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Thread.Thread import recuperation 
from Article.Chat_GPT_filtre import generer_filtre_veille 


from Article.Chat_GPT_Article import generer_article_veille 

from video.setup_video import  setup


from video.Chat_GPT_Video_filtre import  creation_filtre_video
from python.src.informatique.video.creation_word_video import  création_mot_video
from python.src.informatique.video.Creation_script_video import creation_script_video 

from video.Recuperation_Video import  recuperation_videos


from video.Voice_script import  voice_videos

from python.src.informatique.video.rush_adjustment import  ajustement_rush
from python.src.informatique.video.Rush_assembly import  assamblage_rush
from python.src.informatique.video.Subtitle_creation import  crated_subtitle
from python.src.informatique.video.assembly_under_rush_title import  assamblage_sous_titre_rush

def retry(func, max_attempts=5, error_message="Erreur lors de la récupération"):
    attempt = 0
    while attempt < max_attempts:
        try:
            func()
            break  # Sortie de la boucle si succès
        except Exception as e:
            print(f"{error_message}. Tentative {attempt + 1}/{max_attempts}. Erreur: {e}")
            attempt += 1
            if attempt == max_attempts:
                print("Nombre maximal de tentatives atteint. Abandon de la fonction.")

def main():
    #recuperation()
    #setup()
    #generer_filtre_veille ()
    #generer_article_veille()
    retry(creation_filtre_video, 1)  # Relance 1 fois
    retry(création_mot_video, 1)     # Relance 1 fois
    retry(creation_script_video, 1)
    retry(recuperation_videos, 10)
    setup()
    retry(voice_videos, 10)
    retry(ajustement_rush, 10)       
    retry(assamblage_rush, 10)       # dans la même séquence de réessai si nécessaire.
    retry(crated_subtitle, 10)       # Pareil pour crated_subtitle et assamblage_sous_titre_rush.
    retry(assamblage_sous_titre_rush, 10)

if __name__ == "__main__":
    main()