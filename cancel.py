from email import Email
from event import Event
from notificationmethod import NotificationMethod
from telegram import Telegram
from student import Student


class Cancel(Event):
    student: Student
    notificationmethod: NotificationMethod

    def __init__(self, notificationmethod: Email or Telegram):
            self.notificationmethod = notificationmethod

    def event(self, student: Student):
        print("取消課程")
