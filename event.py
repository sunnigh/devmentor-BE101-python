from abc import ABC, abstractmethod
from user import User

class Event(ABC):
    @abstractmethod
    def event(self, user: User):
        pass

