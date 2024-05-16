from event import Event
from student import Student
from user import User


class Reserve(Event):
    def launch_event(self):
        return 'reserve'
