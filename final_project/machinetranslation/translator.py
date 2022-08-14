"""Bot Translator"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    version = '2022-08-14',
    authenticator = authenticator
)


def english_to_french(english_text):
    """ English to French"""
    french_text = translator.translate(text = english_text, model_id = 'en-fr').get_result()
    print(json.dumps(french_text, indent=2, ensure_ascii=False))
    return french_text

def french_to_english(french_text):
    """French to English"""
    english_text = translator.translate(text = french_text, model_id = 'fr-en').get_result()
    print(json.dumps(french_text, indent=2, ensure_ascii=False))
    return english_text
 