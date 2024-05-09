from typing import List

import enus
from email import Email
from event import Event
from guest import Guest
from notificationmethod import NotificationMethod
from sms import Sms
from student import Student
from user import User


class Signup(Event):
    notification_method: List[NotificationMethod] = []
    guest: Guest

    def __init__(self):
        self.notification_method = []

    def add_notification_method(self, notification_method: NotificationMethod):
        self.notification_method.append(notification_method)

    def event(self, guest: User):
        username: str = guest.username
        sentence: str = guest.language.get_sentence('123')
        notify_sentence = "{} {}".format(username, sentence)
        for method in self.notification_method:
            method.notify(notify_sentence)



