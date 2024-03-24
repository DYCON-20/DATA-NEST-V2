import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from Setting.setting_bdd import  setting_bdd
from Thread.Thread import recuperation 


def setup() : 
    setting_bdd()
    recuperation()



