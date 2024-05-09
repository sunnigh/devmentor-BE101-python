import enus
from language_system import LanguageSystem
from zhtw import Zhtw


class User:
    language: LanguageSystem

    def __init__(self, username: str, lang: LanguageSystem):
        self.language = lang
        self.username = username

    def do(self):
        print(self.language.get_sentence("123"))
        print(self.username)



