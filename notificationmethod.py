from abc import ABC, abstractmethod


class NotificationMethod(ABC):
    @abstractmethod
    def notify(self, sentence: str):
        pass
