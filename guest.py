import self
from event import Event
from notificationmethod import NotificationMethod
from signup import Signup
from sms import Sms
from user import User


class Guest(User):
    event: Event

    def __init__(self, event: Signup):
        self.event = event

    def do(self):
        self.event.event()


guest = Guest(Signup(Sms.notify(self)))
guest.do()
