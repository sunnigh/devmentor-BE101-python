from language_system import LanguageSystem


class User:
    language: LanguageSystem

    def __init__(self, lang: LanguageSystem):
        self.language = lang



