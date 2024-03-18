from .Thread_ajout_bdd import recuperationbdd
from typing import Dict
import json
import jmespath
from parsel import Selector
from nested_lookup import nested_lookup
from playwright.sync_api import sync_playwright
import pandas as pd  

# Définissez la fonction pour parser un fil
# Define the function to parse a thread
def parse_thread(post: Dict) -> Dict:
    """Parse Twitter tweet JSON dataset for the specified fields"""
    result = jmespath.search(
        """{
        id_Thread: post.id,
        User: post.user.username,
        Texte: post.caption.text,
        Lien_images: post.carousel_media[].image_versions2.candidates[1].url,
        Lien_video: post.video_versions[].url,
        Date_Thread: post.taken_at
    }""",
        post,
    )
    # Vérifiez si Lien_images est None avant de tenter de l'itérer
    # Check if Lien_images is None before attempting to iterate over it
    result["Lien_images"] = [str(url) for url in (result["Lien_images"] or [])]
    # Vérifiez si Lien_video est None avant de tenter de l'itérer
    # Check if Lien_video is None before attempting to iterate over it
    result["Lien_video"] = [str(url) for url in (result["Lien_video"] or [])]
    
    result["Lien_de_la_page"] = f"https://www.threads.net/@{result['User']}" # Lien de la page / Page link
    return result

# Définissez la fonction pour extraire les fils à partir d'une URL
# Define the function to scrape threads from a URL
def scrape_thread(url: str) -> None:
    """Scrape Threads post and replies from a given URL"""
    # Créez une liste pour stocker les fils
    # Create a list to store the threads
    threads_list = []

    # Utilisez Playwright pour naviguer sur la page
    # Use Playwright to navigate to the page
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        # Accédez à l'URL et attendez le chargement de la page
        # Go to the URL and wait for the page to load
        page.goto(url)
        page.wait_for_selector("[data-pressable-container=true]")

        # Trouvez tous les ensembles de données cachés
        # Find all hidden datasets
        selector = Selector(page.content())
        hidden_datasets = selector.css('script[type="application/json"][data-sjs]::text').getall()

        # Trouvez les ensembles de données contenant des informations sur les fils
        # Find datasets containing information on threads
        for hidden_dataset in hidden_datasets:
            if '"ScheduledServerJS"' not in hidden_dataset:
                continue
            if "thread_items" not in hidden_dataset:
                continue
            data = json.loads(hidden_dataset)
            thread_items = nested_lookup("thread_items", data)
            if not thread_items:
                continue
            threads = [parse_thread(t) for thread_item in thread_items for t in thread_item]
            
            # Ajoutez les fils à la liste
            # Add the threads to the list
            threads_list.extend(threads)
            
            # Vérifiez si les 10 premières valeurs de id_Thread ont été enregistrées
            # Check if the top 10 thread IDs have been recorded
            if len(threads_list) >= 10:
                break

    # Créez un DataFrame à partir de la liste de dictionnaires (threads_list)
    # Create a DataFrame from the list of dictionaries (threads_list)
    df = pd.DataFrame(threads_list)

    # Affichez les résultats au format demandé pour les trois premiers résultats
    # Display the results in the requested format for the top three results
    for idx, thread in df.head(5).iterrows():
        result_tuple = (
            thread['id_Thread'],
            thread['User'],
            thread['Texte'],
            '' if not thread['Lien_images'] else thread['Lien_images'][0],
            '' if not thread['Lien_video'] else thread['Lien_video'][0],
            thread['Date_Thread'],
            ""
        )

        result_list = list(result_tuple)
        recuperationbdd([result_tuple]) # Sauvegardez les résultats dans la base dedonnées / Save the results to the database
