import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
#from Thread.Thread import recuperation 
#from Article.Chat_GPT_filtre import generer_filtre_veille 
#from Article.Chat_GPT_Article import generer_article_veille 
#from video.Chat_GPT_Video_filtre import  creation_filtre_video
#from video.Chat_GPT_Video_mot import  création_mot_video
from video.Chat_GPT_Video_Script import creation_script_video

from video.Recuperation_Video import  recuperation_videos
from video.Voice_script import  voice_videos

from video.Montage_Video_1 import  ajustement_rush
from video.Montage_Video_2 import  assamblage_rush
from video.Montage_Video_3 import  assamblage_sous_titre_rush


def main():
    #recuperation()
    #generer_filtre_veille()
    #generer_article_veille()
    #creation_filtre_video()
    #création_mot_video()
    creation_script_video()
    recuperation_videos()
    voice_videos()
    ajustement_rush()
    assamblage_rush()
    assamblage_sous_titre_rush()
if __name__ == "__main__":
    main()