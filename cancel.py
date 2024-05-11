from typing import List

from email import Email
from event import Event
from notificationmethod import NotificationMethod
from telegram import Telegram
from student import Student


class Cancel(Event):
    student: Student
    notification_method: List[NotificationMethod] = []

    def __init__(self):
        self.notification_method = []

    def add_notification_method(self, notification_method: NotificationMethod):
        self.notification_method.append(notification_method)

    def launch(self, student: Student):
        username: str = student.username
        sentence: str = student.language.get_sentence('cancel')
        notify_sentence = "{} {}".format(username, sentence)
        for method in self.notification_method:
            method.notify(notify_sentence)
