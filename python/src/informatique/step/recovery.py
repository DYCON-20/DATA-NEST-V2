import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from Setting.source import Source
from Setting.Chat_GPT_filtre import generer_filtre_veille 


def recovery() : 
    Source()
    generer_filtre_veille()

