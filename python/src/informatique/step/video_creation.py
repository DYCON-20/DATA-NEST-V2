import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from video.Voice_script import  voice_videos

from video.Montage_Video_1 import  ajustement_rush
from video.Montage_Video_2 import  assamblage_rush
from video.Montage_Video_3 import  crated_subtitle
from video.Montage_Video_4 import  assamblage_sous_titre_rush
from video.Chat_GPT_Video_mot import  création_mot_video
from video.Chat_GPT_Video_Script import creation_script_video 
from step.setup import  setup

from video.Recuperation_Video import  recuperation_videos


def generer_video() : 
    setup()
    création_mot_video()
    creation_script_video()
    recuperation_videos()
    voice_videos()
    ajustement_rush()
    assamblage_rush()
    crated_subtitle()
    assamblage_sous_titre_rush()