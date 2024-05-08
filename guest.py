import self
from event import Event
from notificationmethod import NotificationMethod
from signup import Signup
from sms import Sms
from user import User


class Guest(User):
    event: Event

    def __init__(self):
        pass

    def do(self,event: Signup):
        event.event()


guest = Guest()
guest.do(Signup(Sms().notify()))
