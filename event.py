from abc import ABC, abstractmethod
from user import User

class Event(ABC):
    @abstractmethod
    def launch(self, user: User):
        pass

