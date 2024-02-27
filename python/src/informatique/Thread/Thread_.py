import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Thread_Recuperation import scrape_thread
from Thread_source import Source

def afficher():
    resultat_afficher = []
    for url in Source:
        try:
            result = scrape_thread(url)
            resultat_afficher.append(result)
        except Exception as e:
            print(f"Erreur lors du scraping de {url}: {e}")
    return resultat_afficher

# Appeler la fonction afficher() et imprimer les résultats
resultat_afficher = afficher()
print(resultat_afficher)
