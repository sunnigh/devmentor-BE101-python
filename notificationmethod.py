from abc import ABC, abstractmethod


class NotificationMethod(ABC):

    def notify(self, sentence: str):
        print("{} by {}".format(sentence, self.launch_method()))

    @abstractmethod
    def launch_method(self):
        pass
