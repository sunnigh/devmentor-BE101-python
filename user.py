import enus
from language_system import LanguageSystem
from zhtw import Zhtw


class User:
    language: LanguageSystem

    def __init__(self, username: str, lang: LanguageSystem):
        self.language = lang
        self.username = username

    def do(self):
        if self.language == enus:
            self.event.event_en()
        elif self.language == zhtw
            self.event.event_tw()
        print(self.username)



