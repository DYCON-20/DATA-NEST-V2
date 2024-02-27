import os
import base64
import argparse
import requests
import random
import re
import textwrap
import shutil
import datetime
from playsound import playsound

# Constants
API_DOMAINS = [
    "https://api16-normal-c-useast1a.tiktokv.com",
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

VOICES = [
    # DISNEY VOICES
    'en_us_ghostface',            # Ghost Face
    'en_us_chewbacca',            # Chewbacca
    'en_us_c3po',                 # C3PO
    'en_us_stitch',               # Stitch
    'en_us_stormtrooper',         # Stormtrooper
    'en_us_rocket',               # Rocket

    # ENGLISH VOICES
    'en_au_001',                  # English AU - Female
    'en_au_002',                  # English AU - Male
    'en_uk_001',                  # English UK - Male 1
    'en_uk_003',                  # English UK - Male 2
    'en_us_001',                  # English US - Female (Int. 1)
    'en_us_002',                  # English US - Female (Int. 2)
    'en_us_006',                  # English US - Male 1
    'en_us_007',                  # English US - Male 2
    'en_us_009',                  # English US - Male 3
    'en_us_010',                  # English US - Male 4

    # EUROPE VOICES
    'fr_001',                     # French - Male 1
    'fr_002',                     # French - Male 2
    'de_001',                     # German - Female
    'de_002',                     # German - Male
    'es_002',                     # Spanish - Male

    # AMERICA VOICES
    'es_mx_002',                  # Spanish MX - Male
    'br_001',                     # Portuguese BR - Female 1
    'br_003',                     # Portuguese BR - Female 2
    'br_004',                     # Portuguese BR - Female 3
    'br_005',                     # Portuguese BR - Male

    # ASIA VOICES
    'id_001',                     # Indonesian - Female
    'jp_001',                     # Japanese - Female 1
    'jp_003',                     # Japanese - Female 2
    'jp_005',                     # Japanese - Female 3
    'jp_006',                     # Japanese - Male
    'kr_002',                     # Korean - Male 1
    'kr_003',                     # Korean - Female
    'kr_004',                     # Korean - Male 2

    # SINGING VOICES
    'en_female_f08_salut_damour',  # Alto
    'en_male_m03_lobby',           # Tenor
    'en_female_f08_warmy_breeze',  # Warmy Breeze
    'en_male_m03_sunshine_soon',   # Sunshine Soon

    # OTHER
    'en_male_narration',           # narrator
    'en_male_funny',               # wacky
    'en_female_emotional',         # peaceful
]

BATCH_DIR = './batch/'

def make_request(session_id, text_speaker, req_text, api_domain):
    req_text = req_text.replace("+", "plus").replace(" ", "+").replace("&", "and")

    headers = {
        'User-Agent': USER_AGENT,
        'Cookie': f'sessionid={session_id}'
    }

    api_url = f"{api_domain}{API_PATH}"

    params = {
        'text_speaker': text_speaker,
        'req_text': req_text,
        'speaker_map_type': 0,
        'aid': 1233
    }

    response = requests.post(api_url, headers=headers, params=params)

    if response.status_code == 200:
        response_data = response.json()
        if "message" in response_data:
            if response_data["message"] == "Couldn't load speech. Try again.":
                raise Exception("Session ID is invalid")
        return response_data
    elif response.status_code == 400:
        raise Exception(f"Bad request. Status code: {response.status_code}")
    elif response.status_code == 401:
        raise Exception(f"Unauthorized. Status code: {response.status_code}")
    elif response.status_code == 403:
        raise Exception(f"Forbidden. Status code: {response.status_code}")
    elif response.status_code == 404:
        raise Exception(f"Not Found. Status code: {response.status_code}")
    elif response.status_code == 500:
        raise Exception(f"Internal server error. Status code: {response.status_code}")
    elif response.status_code == 502:
        raise Exception(f"Bad Gateway. Status code: {response.status_code}")
    elif response.status_code == 503:
        raise Exception(f"Service Unavailable. Status code: {response.status_code}")
    else:
        raise Exception(f"Failed to make a request to domain {api_domain}. Status code: {response.status_code}")

OUTPUT_DIR = 'python/src/informatique/Video_traitement/'  # Nouveau chemin de sortie


def tts(session_id, text_speaker="en_us_002", req_text="TikTok Text To Speech", filename='audio_video.mp3', play=False):
    filename = os.path.join(OUTPUT_DIR, filename)
    try:
        for index, api_domain in enumerate(API_DOMAINS):
            print(f"Testing domain {index + 1}: {api_domain}")
            try:
                response_data = make_request(session_id, text_speaker, req_text, api_domain)

                if response_data["message"] == "Couldn't load speech. Try again.":
                    print(f"Error: Session ID is invalid for domain {index + 1}")
                    continue

                vstr = response_data["data"]["v_str"]
                msg = response_data["message"]
                scode = response_data["status_code"]
                log = response_data["extra"]["log_id"]
                dur = response_data["data"]["duration"]
                spkr = response_data["data"]["speaker"]

                b64d = base64.b64decode(vstr)

                with open(filename, "wb") as out:
                    out.write(b64d)

                output_data = {
                    "status": msg.capitalize(),
                    "status_code": scode,
                    "duration": dur,
                    "speaker": spkr,
                    "log": log
                }

                print(output_data)

                if play:
                    playsound(filename)
                    os.remove(filename)

                return output_data
            except Exception as e:
                print(f"Error: {e}")

        print("Error: Failed to make a request to all domains")
        exit(1)  # Exit the program if all domains fail
    except Exception as e:
        print(f"Error: {e}")
        exit(1)  # Exit the program if there's an error

def batch_create():
    try:
        current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = os.path.join(OUTPUT_DIR, f'audio_video_{current_time}.mp3')  # Modification du chemin et du nom de fichier

        out = open(filename, 'wb')

        def sorted_alphanumeric(data):
            convert = lambda text: int(text) if text.isdigit() else text.lower()
            alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
            return sorted(data, key=alphanum_key)

        if os.path.exists(BATCH_DIR):
            shutil.rmtree(BATCH_DIR)

        os.makedirs(BATCH_DIR)

        for i, item in enumerate(sorted_alphanumeric(os.listdir(BATCH_DIR))):
            filestuff = open(f'{BATCH_DIR}{item}', 'rb').read()
            out.write(filestuff)

        out.close()
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple Python script to interact with the TikTok TTS API")
    parser.add_argument("-v", "--voice", help="the code of the desired voice")
    parser.add_argument("-t", "--text", help="the text to be read")
    parser.add_argument("-s", "--session", help="account session id")
    parser.add_argument("-f", "--file", help="use this if you wanna use 'text.txt'")
    parser.add_argument("-n", "--name", help="The name for the output file (.mp3)")
    parser.add_argument("-p", "--play", action='store_true', help="use this if you want to play your output")
    args = parser.parse_args()

    text_speaker = args.voice
    play = args.play

    if args.file is not None:
        req_text = open(args.file, 'r', errors='ignore', encoding='utf-8').read()
    else:
        req_text = args.text if args.text else 'TikTok Text To Speech'

    if not text_speaker:
        text_speaker = 'en_us_002'
        print('You need to have a voice! (See README.md)')

    if text_speaker == "random":
        text_speaker = random.choice(VOICES)

    filename = args.name if args.name else 'audio_video.mp3'

    if not args.session:
        print('FATAL: You need to have a TikTok session ID!')
        exit(1)

    if args.file:
        try:
            chunk_size = 200
            textlist = textwrap.wrap(req_text, width=chunk_size, break_long_words=True, break_on_hyphens=False)

            if os.path.exists(BATCH_DIR):
                shutil.rmtree(BATCH_DIR)

            os.makedirs(BATCH_DIR)

            for i, item in enumerate(textlist):
                tts(args.session, text_speaker, item, f'{BATCH_DIR}{i}.mp3')

            batch_create(filename)

            for item in os.listdir(BATCH_DIR):
                os.remove(f'{BATCH_DIR}{item}')

            os.removedirs(BATCH_DIR)
        except Exception as e:
            print(f"Error: {e}")
    else:
        tts(args.session, text_speaker, req_text, filename, play)

if __name__ == "__main__":
    main()
