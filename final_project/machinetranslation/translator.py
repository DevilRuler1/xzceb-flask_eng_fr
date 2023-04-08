"""
Translator Service between English and French
"""

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

URL = ""
API = ""

authenticator = IAMAuthenticator(API)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)


def eng_to_french(text):
    """
    Function to translate from english to french
    """
    french = language_translator.translate(text=text, model_id="en-fr").get_result()
    return french.get("translations")[0].get("translation")

def fench_to_eng(text):
    """
    Function to translate from french to english
    """
    english = language_translator.translate(text=text, model_id="fr-en").get_result()
    return english.get("translations")[0].get("translation")
