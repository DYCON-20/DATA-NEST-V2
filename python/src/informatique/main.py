from Thread.Thread_Recuperation import scrape_thread
from Thread.Thread_source import Source

def afficher():
    resultat_afficher = []
    for url in Source:
        result = scrape_thread(url)
        resultat_afficher.append(result)
    return resultat_afficher

if __name__ == "__main__":
    resultat_afficher = afficher()

    print(resultat_afficher)


