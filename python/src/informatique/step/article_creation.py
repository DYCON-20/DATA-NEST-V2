import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from Article.Chat_GPT_Article import generer_article_veille 

def generer_article() : 
    generer_article_veille()

