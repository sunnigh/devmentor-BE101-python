from event import Event
from student import Student
from user import User


class Cancel(Event):

    def launch_event(self):
        return 'cancel'
