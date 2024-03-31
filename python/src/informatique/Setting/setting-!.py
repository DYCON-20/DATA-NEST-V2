import mysql.connector
from openai import OpenAI


from forex_python.converter import CurrencyRates


Theme = "Technology"

c = CurrencyRates()
rate = c.get_rate('USD', 'EUR')  



def connect_db():
    conn = mysql.connector.connect(
        host='',
        port=,
        user='root',
        password='',
        database='Data_Nest'
    )
    return conn

def connect_db_creat():
    conn = mysql.connector.connect(
        host='',
        port=,
        user='',
        password='',
    )
    return conn

client = OpenAI(api_key='')

API_KEY = ''

TIKTOK_id = ''

AssemblyAI = ''

DISCORD_KEY = ''

WEBHOOK = ""

LANGUAGE = "Francais"

LANGUAGE_VOICE ="fr_001"

LANGUAGE_Subtitle ="fr"
#'de', 'en', 'en_au', 'en_uk', 'en_us', 'es', 'fi', 'fr', 'hi', 'it', 'ja', 'ko', 'nl', 'pl', 'pt', 'ru', 'tr', 'uk', 'vi', 'zh'

#VOICES = [
        #'en_us_ghostface', 'en_us_chewbacca', 'en_us_c3po', 'en_us_stitch',
        #'en_us_stormtrooper', 'en_us_rocket', 'en_au_001', 'en_au_002',
        #'en_uk_001', 'en_uk_003', 'en_us_001', 'en_us_002', 'en_us_006',
        #'en_us_007', 'en_us_009', 'en_us_010', 'fr_001', 'fr_002', 'de_001',
        #'de_002', 'es_002', 'es_mx_002', 'br_001', 'br_003', 'br_004',
        #'br_005', 'id_001', 'jp_001', 'jp_003', 'jp_005', 'jp_006', 'kr_002',
        #'kr_003', 'kr_004', 'en_female_f08_salut_damour', 'en_male_m03_lobby',
        #'en_female_f08_warmy_breeze', 'en_male_m03_sunshine_soon', 'en_male_narration',
        #'en_male_funny', 'en_female_emotional',
#]




TEXTE_INTRO = " intro "
TEXTE_OUTRO = "outro"