from event import Event
from guest import Guest
from user import User


class Signup(Event):

    def launch_event(self):
        return 'signup'
