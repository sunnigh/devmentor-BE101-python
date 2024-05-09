import enus
from email import Email
from event import Event
from guest import Guest
from notificationmethod import NotificationMethod
from sms import Sms


class Signup(Event):
    notificationmethod: NotificationMethod
    guest: Guest


    def __init__(self, notificationmethod: Sms or Email):
        self.notificationmethod = notificationmethod

    def event(self, guest: Guest):
        print('註冊')


signup = Signup(Sms())
signup.event(Guest())
