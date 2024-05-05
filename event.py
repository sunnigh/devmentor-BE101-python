from abc import ABC,abstractmethod
class Event(ABC):
    @abstractmethod
    def event(self):
        pass
    pass