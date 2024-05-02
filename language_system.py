from abc import ABC, abstractmethod


class LanguageSystem(ABC):

    @abstractmethod
    def language(self):
        pass
