import self
from event import Event
from notificationmethod import NotificationMethod
from sms import Sms
from user import User


class Guest(User):
    event: Event

    def __init__(self):
        pass


