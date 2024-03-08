import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import base64
import argparse
import requests
from playsound import playsound
from datetime import datetime, timedelta

from setting import TIKTOK_id
from pydub import AudioSegment
import requests
import base64
import os
from playsound import playsound

from setting import Theme


datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

def voice_videos():


    # Assuming setting.py contains the necessary database connection parameters
    from setting import connect_db
    from datetime import datetime, timedelta

    # Connect to the database
    conn = connect_db()
    c = conn.cursor()

    # Calculate yesterday's date in YYYY-MM-DD format
    date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    # Execute the query to retrieve data dated yesterday
    c.execute('SELECT script_article_1, script_article_2, script_article_3, script_article_4, script_article_5 FROM Video_script WHERE date = %s', (date_du_jour_avant,))

    # Retrieve the first result (if available)
    resultat = c.fetchone()

    if resultat:
        # Assign the results to variables
        data1, data2, data3, data4, data5 = resultat

        # Display to confirm the values
        print("Recup")
    else:
        print("Aucun résultat trouvé pour la date d'hier.")
        # Initialize variables if no result is found
        data1 = data2 = data3 = data4 = data5 = None

    # Close the cursor
    c.close()

    # Close the connection to the database
    conn.close()

    # You can now use `data1`, `data2`, `data3`, `data4`, `data5` for other operations







    # Constants
    API_DOMAINS = [
        "https://api16-normal-c-useast2a.tiktokv.com",
        "https://api16-normal-c-useast1a.tiktokv.com",
        "https://api16-core-c-useast1a.tiktokv.com",
        "https://api16-normal-useast5.us.tiktokv.com",
        "https://api16-core.tiktokv.com",
        "https://api16-core-useast5.us.tiktokv.com",
        "https://api19-core-c-useast1a.tiktokv.com",
        "https://api-core.tiktokv.com",
        "https://api-normal.tiktokv.com",
        "https://api19-normal-c-useast1a.tiktokv.com",
        "https://api16-core-c-alisg.tiktokv.com",
        "https://api16-normal-c-alisg.tiktokv.com",
        "https://api22-core-c-alisg.tiktokv.com",
        "https://api16-normal-c-useast2a.tiktokv.com",
    ]
    API_PATH = "/media/api/text/speech/invoke/"
    USER_AGENT = "com.zhiliaoapp.musically/2022600030 (Linux; U; Android 7.1.2; es_ES; SM-G988N; Build/NRD90M;tt-ok/3.12.13.1)"

    # Fusion des catégories de voix en une seule liste pour simplifier
    VOICES = [
        'en_us_ghostface', 'en_us_chewbacca', 'en_us_c3po', 'en_us_stitch',
        'en_us_stormtrooper', 'en_us_rocket', 'en_au_001', 'en_au_002',
        'en_uk_001', 'en_uk_003', 'en_us_001', 'en_us_002', 'en_us_006',
        'en_us_007', 'en_us_009', 'en_us_010', 'fr_001', 'fr_002', 'de_001',
        'de_002', 'es_002', 'es_mx_002', 'br_001', 'br_003', 'br_004',
        'br_005', 'id_001', 'jp_001', 'jp_003', 'jp_005', 'jp_006', 'kr_002',
        'kr_003', 'kr_004', 'en_female_f08_salut_damour', 'en_male_m03_lobby',
        'en_female_f08_warmy_breeze', 'en_male_m03_sunshine_soon', 'en_male_narration',
        'en_male_funny', 'en_female_emotional',
    ]

    date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    OUTPUT_DIR =  f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio"

    # Définissez vos variables ici
    session_id = TIKTOK_id
    text_speaker = "fr_002"
    filename = 'audio_article_1.mp3'
    req_text = f"{data1}"

    play = False

    def make_request(session_id, text_speaker, req_text, api_domain):
        headers = {'User-Agent': USER_AGENT, 'Cookie': f'sessionid={session_id}'}
        params = {
            'text_speaker': text_speaker,
            'req_text': req_text, 
            'speaker_map_type': 0,
            'aid': 1233
        }
        response = requests.post(f"{api_domain}{API_PATH}", headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def tts(session_id, text_speaker, req_text, filename, play):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        for api_domain in API_DOMAINS:
            try:
                response_data = make_request(session_id, text_speaker, req_text, api_domain)
                # Vérifiez si la réponse contient le message d'erreur attendu
                if response_data.get("message") == "Couldn't load speech. Try again.":
                    continue  # Essayer avec le domaine suivant
                # Écriture du fichier audio
                with open(filepath, "wb") as out:
                    out.write(base64.b64decode(response_data["data"]["v_str"]))

                audio = AudioSegment.from_file(filepath)
                silence = AudioSegment.silent(duration=500)  # 500 ms de silence
                audio += silence
                audio.export(filepath, format="mp3")

                if play:
                    playsound(filepath)
                print(f"Audio saved to {filepath}")
                return  # Succès, fin de la fonction
            except Exception as e:
                print(f"Failed to make a request to {api_domain}. Error: {e}")
        
        raise Exception("Failed to make a request to all domains.")

    # Exécution
    try:
        tts(session_id, text_speaker, req_text, filename, play)
    except Exception as e:
        print(e)

        
    # Définissez vos variables ici
    session_id = "0741b49e02bc59213d450c65e4430382"
    text_speaker = "fr_002"
    filename = 'audio_article_2.mp3'
    req_text = f"{data2}"

    play = False

    def make_request(session_id, text_speaker, req_text, api_domain):
        headers = {'User-Agent': USER_AGENT, 'Cookie': f'sessionid={session_id}'}
        params = {
            'text_speaker': text_speaker,
            'req_text': req_text, 
            'speaker_map_type': 0,
            'aid': 1233
        }
        response = requests.post(f"{api_domain}{API_PATH}", headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def tts(session_id, text_speaker, req_text, filename, play):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        for api_domain in API_DOMAINS:
            try:
                response_data = make_request(session_id, text_speaker, req_text, api_domain)
                # Vérifiez si la réponse contient le message d'erreur attendu
                if response_data.get("message") == "Couldn't load speech. Try again.":
                    continue  # Essayer avec le domaine suivant
                # Écriture du fichier audio
                with open(filepath, "wb") as out:
                    out.write(base64.b64decode(response_data["data"]["v_str"]))
                audio = AudioSegment.from_file(filepath)
                silence = AudioSegment.silent(duration=500)  # 500 ms de silence
                audio += silence
                audio.export(filepath, format="mp3")                    
                if play:
                    playsound(filepath)
                print(f"Audio saved to {filepath}")
                return  # Succès, fin de la fonction
            except Exception as e:
                print(f"Failed to make a request to {api_domain}. Error: {e}")
        
        raise Exception("Failed to make a request to all domains.")

    # Exécution
    try:
        tts(session_id, text_speaker, req_text, filename, play)
    except Exception as e:
        print(e)


    # Définissez vos variables ici
    session_id = "0741b49e02bc59213d450c65e4430382"
    text_speaker = "fr_002"
    filename = 'audio_article_3.mp3'
    req_text = f"{data3}"

    play = False

    def make_request(session_id, text_speaker, req_text, api_domain):
        headers = {'User-Agent': USER_AGENT, 'Cookie': f'sessionid={session_id}'}
        params = {
            'text_speaker': text_speaker,
            'req_text': req_text, 
            'speaker_map_type': 0,
            'aid': 1233
        }
        response = requests.post(f"{api_domain}{API_PATH}", headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def tts(session_id, text_speaker, req_text, filename, play):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        for api_domain in API_DOMAINS:
            try:
                response_data = make_request(session_id, text_speaker, req_text, api_domain)
                # Vérifiez si la réponse contient le message d'erreur attendu
                if response_data.get("message") == "Couldn't load speech. Try again.":
                    continue  # Essayer avec le domaine suivant
                # Écriture du fichier audio
                with open(filepath, "wb") as out:
                    out.write(base64.b64decode(response_data["data"]["v_str"]))
                audio = AudioSegment.from_file(filepath)
                silence = AudioSegment.silent(duration=500)  # 500 ms de silence
                audio += silence
                audio.export(filepath, format="mp3")                    
                if play:
                    playsound(filepath)
                print(f"Audio saved to {filepath}")
                return  # Succès, fin de la fonction
            except Exception as e:
                print(f"Failed to make a request to {api_domain}. Error: {e}")
        
        raise Exception("Failed to make a request to all domains.")

    # Exécution
    try:
        tts(session_id, text_speaker, req_text, filename, play)
    except Exception as e:
        print(e)



    # Définissez vos variables ici
    session_id = "0741b49e02bc59213d450c65e4430382"
    text_speaker = "fr_002"
    filename = 'audio_article_4.mp3'
    req_text = f"{data4}"

    play = False

    def make_request(session_id, text_speaker, req_text, api_domain):
        headers = {'User-Agent': USER_AGENT, 'Cookie': f'sessionid={session_id}'}
        params = {
            'text_speaker': text_speaker,
            'req_text': req_text, 
            'speaker_map_type': 0,
            'aid': 1233
        }
        response = requests.post(f"{api_domain}{API_PATH}", headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def tts(session_id, text_speaker, req_text, filename, play):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        for api_domain in API_DOMAINS:
            try:
                response_data = make_request(session_id, text_speaker, req_text, api_domain)
                # Vérifiez si la réponse contient le message d'erreur attendu
                if response_data.get("message") == "Couldn't load speech. Try again.":
                    continue  # Essayer avec le domaine suivant
                # Écriture du fichier audio
                with open(filepath, "wb") as out:
                    out.write(base64.b64decode(response_data["data"]["v_str"]))
                audio = AudioSegment.from_file(filepath)
                silence = AudioSegment.silent(duration=500)  # 500 ms de silence
                audio += silence
                audio.export(filepath, format="mp3")                    
                if play:
                    playsound(filepath)
                print(f"Audio saved to {filepath}")
                return  # Succès, fin de la fonction
            except Exception as e:
                print(f"Failed to make a request to {api_domain}. Error: {e}")
        
        raise Exception("Failed to make a request to all domains.")

    # Exécution
    try:
        tts(session_id, text_speaker, req_text, filename, play)
    except Exception as e:
        print(e)

    # Définissez vos variables ici
    session_id = "0741b49e02bc59213d450c65e4430382"
    text_speaker = "fr_002"
    filename = 'audio_article_5.mp3'
    req_text = f"{data5}"

    play = False

    def make_request(session_id, text_speaker, req_text, api_domain):
        headers = {'User-Agent': USER_AGENT, 'Cookie': f'sessionid={session_id}'}
        params = {
            'text_speaker': text_speaker,
            'req_text': req_text, 
            'speaker_map_type': 0,
            'aid': 1233
        }
        response = requests.post(f"{api_domain}{API_PATH}", headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def tts(session_id, text_speaker, req_text, filename, play):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        for api_domain in API_DOMAINS:
            try:
                response_data = make_request(session_id, text_speaker, req_text, api_domain)
                # Vérifiez si la réponse contient le message d'erreur attendu
                if response_data.get("message") == "Couldn't load speech. Try again.":
                    continue  # Essayer avec le domaine suivant
                # Écriture du fichier audio
                with open(filepath, "wb") as out:
                    out.write(base64.b64decode(response_data["data"]["v_str"]))
                audio = AudioSegment.from_file(filepath)
                silence = AudioSegment.silent(duration=500)  # 500 ms de silence
                audio += silence
                audio.export(filepath, format="mp3")                    
                if play:
                    playsound(filepath)
                print(f"Audio saved to {filepath}")
                return  # Succès, fin de la fonction
            except Exception as e:
                print(f"Failed to make a request to {api_domain}. Error: {e}")
        
        raise Exception("Failed to make a request to all domains.")

    # Exécution
    try:
        tts(session_id, text_speaker, req_text, filename, play)
    except Exception as e:
        print(e)


 # Définissez vos variables ici
    session_id = "0741b49e02bc59213d450c65e4430382"
    text_speaker = "fr_002"
    filename = 'intro.mp3'
    req_text = " Bonjour a tous bienvenue sur cette veile informatique 5 nouvelle en 1 minute "

    play = False

    def make_request(session_id, text_speaker, req_text, api_domain):
        headers = {'User-Agent': USER_AGENT, 'Cookie': f'sessionid={session_id}'}
        params = {
            'text_speaker': text_speaker,
            'req_text': req_text, 
            'speaker_map_type': 0,
            'aid': 1233
        }
        response = requests.post(f"{api_domain}{API_PATH}", headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def tts(session_id, text_speaker, req_text, filename, play):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        for api_domain in API_DOMAINS:
            try:
                response_data = make_request(session_id, text_speaker, req_text, api_domain)
                # Vérifiez si la réponse contient le message d'erreur attendu
                if response_data.get("message") == "Couldn't load speech. Try again.":
                    continue  # Essayer avec le domaine suivant
                # Écriture du fichier audio
                with open(filepath, "wb") as out:
                    out.write(base64.b64decode(response_data["data"]["v_str"]))
                audio = AudioSegment.from_file(filepath)
                silence = AudioSegment.silent(duration=500)  # 500 ms de silence
                audio += silence
                audio.export(filepath, format="mp3")                    
                if play:
                    playsound(filepath)
                print(f"Audio saved to {filepath}")
                return  # Succès, fin de la fonction
            except Exception as e:
                print(f"Failed to make a request to {api_domain}. Error: {e}")
        
        raise Exception("Failed to make a request to all domains.")

    # Exécution
    try:
        tts(session_id, text_speaker, req_text, filename, play)
    except Exception as e:
        print(e)


# Définissez vos variables ici
    session_id = "0741b49e02bc59213d450c65e4430382"
    text_speaker = "fr_002"
    filename = 'outro.mp3'
    req_text = " C'est la fin rendez vous demain pour une nouvelle veille "

    play = False

    def make_request(session_id, text_speaker, req_text, api_domain):
        headers = {'User-Agent': USER_AGENT, 'Cookie': f'sessionid={session_id}'}
        params = {
            'text_speaker': text_speaker,
            'req_text': req_text, 
            'speaker_map_type': 0,
            'aid': 1233
        }
        response = requests.post(f"{api_domain}{API_PATH}", headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def tts(session_id, text_speaker, req_text, filename, play):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        for api_domain in API_DOMAINS:
            try:
                response_data = make_request(session_id, text_speaker, req_text, api_domain)
                # Vérifiez si la réponse contient le message d'erreur attendu
                if response_data.get("message") == "Couldn't load speech. Try again.":
                    continue  # Essayer avec le domaine suivant
                # Écriture du fichier audio
                with open(filepath, "wb") as out:
                    out.write(base64.b64decode(response_data["data"]["v_str"]))
                audio = AudioSegment.from_file(filepath)
                silence = AudioSegment.silent(duration=500)  # 500 ms de silence
                audio += silence
                audio.export(filepath, format="mp3")                    
                if play:
                    playsound(filepath)
                print(f"Audio saved to {filepath}")
                return  # Succès, fin de la fonction
            except Exception as e:
                print(f"Failed to make a request to {api_domain}. Error: {e}")
        
        raise Exception("Failed to make a request to all domains.")

    # Exécution
    try:
        tts(session_id, text_speaker, req_text, filename, play)
    except Exception as e:
        print(e)


    pass