import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from video.Voice_script import  voice_videos

from video.Rush_adjustment import  rush_adjustment
from video.Rush_assembly import  rush_assembly
from video.Rubtitle_creation import  subtitle_creation
from video.Assembly_under_rush_title import  assembly_under_rush_title
from video.Creation_word_video import  creation_word_video
from video.Creation_script_video import creation_script_video 
from video.setup_video import setup
from video.Recuperation_Video import  recuperation_videos


def generer_video() : 
    setup()
    creation_word_video()
    creation_script_video()
    recuperation_videos()
    voice_videos()
    rush_adjustment()
    rush_assembly()
    subtitle_creation()
    assembly_under_rush_title()