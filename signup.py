from email import Email
from event import Event
from sms import Sms


class Signup(Event):
    email: Email
    sms: Sms

    def __init__(self, email: Email, sms :Sms):
        self.email = email
        self.sms = sms

    def event(self):
        pass
