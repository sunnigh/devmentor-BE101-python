import enus
from language_system import LanguageSystem


class User:
    language: LanguageSystem

    def __init__(self, username: str, lang: LanguageSystem):
        self.language = lang
        self.username = username

    def do(self):
        print(self.username)


language = enus.Enus()
user = User("Alex", language)
user.do()
