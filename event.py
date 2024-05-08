from abc import ABC, abstractmethod
from user import User

class Event(ABC):
    user: User
    @abstractmethod
    def event(self, user):
        pass

    pass
