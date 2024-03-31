import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import base64
import argparse
import requests
from playsound import playsound
from datetime import datetime, timedelta

from Setting.setting import  TIKTOK_id
from pydub import AudioSegment
import requests
import base64
import os
from playsound import playsound
from Setting.setting import  TEXTE_INTRO, TEXTE_OUTRO


from Setting.setting import  Theme
from Setting.setting import  LANGUAGE_VOICE


datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

def voice_videos():
    try:
        print("-")
        print("🟦 Create voice recording [ B{6/10} ]🟦")

     
        from Setting.setting import  connect_db
        from datetime import datetime, timedelta

     
        conn = connect_db()
        c = conn.cursor()

        date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

        c.execute('SELECT script_article_1, script_article_2, script_article_3, script_article_4, script_article_5 FROM Video_script WHERE date = %s', (date_du_jour_avant,))

        resultat = c.fetchone()

        if resultat:
            data1, data2, data3, data4, data5 = resultat

            print("✅Recovery✅")
        else:
            print("❌No results found for yesterday's date.❌")
            data1 = data2 = data3 = data4 = data5 = None

        c.close()

        conn.close()








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



        date_du_jour_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

        OUTPUT_DIR =  f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio"




        session_id = TIKTOK_id
        text_speaker = LANGUAGE_VOICE
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
     
                    if response_data.get("message") == "Couldn't load speech. Try again.":
                        continue       
     
                    with open(filepath, "wb") as out:
                        out.write(base64.b64decode(response_data["data"]["v_str"]))

                    audio = AudioSegment.from_file(filepath)
                    silence = AudioSegment.silent(duration=500)       
                    audio += silence
                    audio.export(filepath, format="mp3")

                    if play:
                        playsound(filepath)
                    print(f"0️⃣Audio saved to {filepath}0️⃣")
                    return      
                except Exception as e:
                    print(f"Failed to make a request to {api_domain}. Error: {e}")
            
            raise Exception("Failed to make a request to all domains.")

     
        try:
            tts(session_id, text_speaker, req_text, filename, play)
        except Exception as e:
            print(e)

            
            
        session_id = TIKTOK_id
        text_speaker = LANGUAGE_VOICE
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
     
                    if response_data.get("message") == "Couldn't load speech. Try again.":
                        continue       
     
                    with open(filepath, "wb") as out:
                        out.write(base64.b64decode(response_data["data"]["v_str"]))
                    audio = AudioSegment.from_file(filepath)
                    silence = AudioSegment.silent(duration=500)       
                    audio += silence
                    audio.export(filepath, format="mp3")                    
                    if play:
                        playsound(filepath)
                    print(f"1️⃣Audio saved to {filepath}1️⃣")
                    return      
                except Exception as e:
                    print(f"Failed to make a request to {api_domain}. Error: {e}")
            
            raise Exception("Failed to make a request to all domains.")

     
        try:
            tts(session_id, text_speaker, req_text, filename, play)
        except Exception as e:
            print(e)



            
        session_id = TIKTOK_id
        text_speaker = LANGUAGE_VOICE
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
     
                    if response_data.get("message") == "Couldn't load speech. Try again.":
                        continue       
     
                    with open(filepath, "wb") as out:
                        out.write(base64.b64decode(response_data["data"]["v_str"]))
                    audio = AudioSegment.from_file(filepath)
                    silence = AudioSegment.silent(duration=500)       
                    audio += silence
                    audio.export(filepath, format="mp3")                    
                    if play:
                        playsound(filepath)
                    print(f"2️⃣Audio saved to {filepath}2️⃣")
                    return      
                except Exception as e:
                    print(f"Failed to make a request to {api_domain}. Error: {e}")
            
            raise Exception("Failed to make a request to all domains.")

     
        try:
            tts(session_id, text_speaker, req_text, filename, play)
        except Exception as e:
            print(e)


            
        session_id = TIKTOK_id
        text_speaker = LANGUAGE_VOICE
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
     
                    if response_data.get("message") == "Couldn't load speech. Try again.":
                        continue       
     
                    with open(filepath, "wb") as out:
                        out.write(base64.b64decode(response_data["data"]["v_str"]))
                    audio = AudioSegment.from_file(filepath)
                    silence = AudioSegment.silent(duration=500)       
                    audio += silence
                    audio.export(filepath, format="mp3")                    
                    if play:
                        playsound(filepath)
                    print(f"3️⃣Audio saved to {filepath}3️⃣")
                    return      
                except Exception as e:
                    print(f"Failed to make a request to {api_domain}. Error: {e}")
            
            raise Exception("Failed to make a request to all domains.")

     
        try:
            tts(session_id, text_speaker, req_text, filename, play)
        except Exception as e:
            print(e)


            
        session_id = TIKTOK_id
        text_speaker = LANGUAGE_VOICE
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
     
                    if response_data.get("message") == "Couldn't load speech. Try again.":
                        continue       
     
                    with open(filepath, "wb") as out:
                        out.write(base64.b64decode(response_data["data"]["v_str"]))
                    audio = AudioSegment.from_file(filepath)
                    silence = AudioSegment.silent(duration=500)       
                    audio += silence
                    audio.export(filepath, format="mp3")                    
                    if play:
                        playsound(filepath)
                    print(f"4️⃣Audio saved to {filepath}4️⃣")
                    return      
                except Exception as e:
                    print(f"Failed to make a request to {api_domain}. Error: {e}")
            
            raise Exception("Failed to make a request to all domains.")

     
        try:
            tts(session_id, text_speaker, req_text, filename, play)
        except Exception as e:
            print(e)




        
        session_id = TIKTOK_id
        text_speaker = LANGUAGE_VOICE
        filename = 'intro.mp3'
        req_text = TEXTE_INTRO

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
     
                    if response_data.get("message") == "Couldn't load speech. Try again.":
                        continue       
     
                    with open(filepath, "wb") as out:
                        out.write(base64.b64decode(response_data["data"]["v_str"]))
                    audio = AudioSegment.from_file(filepath)
                    silence = AudioSegment.silent(duration=500)       
                    audio += silence
                    audio.export(filepath, format="mp3")                    
                    if play:
                        playsound(filepath)
                    print(f"5️⃣Audio saved to {filepath}5️⃣")
                    return      
                except Exception as e:
                    print(f"Failed to make a request to {api_domain}. Error: {e}")
            
            raise Exception("Failed to make a request to all domains.")

        
        try:
            tts(session_id, text_speaker, req_text, filename, play)
        except Exception as e:
            print(e)


        
        session_id = TIKTOK_id
        text_speaker = LANGUAGE_VOICE
        filename = 'outro.mp3'
        req_text = TEXTE_OUTRO

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
     
                    if response_data.get("message") == "Couldn't load speech. Try again.":
                        continue       
     
                    with open(filepath, "wb") as out:
                        out.write(base64.b64decode(response_data["data"]["v_str"]))
                    audio = AudioSegment.from_file(filepath)
                    silence = AudioSegment.silent(duration=500)       
                    audio += silence
                    audio.export(filepath, format="mp3")                    
                    if play:
                        playsound(filepath)
                    print(f"Audio saved to {filepath}")
                    return      
                except Exception as e:
                    print(f"Failed to make a request to {api_domain}. Error: {e}")
            
            raise Exception("Failed to make a request to all domains.")

        try:
            tts(session_id, text_speaker, req_text, filename, play)
        except Exception as e:
            print(e)


    except Exception as e:
            print(f"""❌❌An error has occurred() ❌❌
            ➡️Here is the error message 🟨{e}🟨 """)

