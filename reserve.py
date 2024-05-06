from email import Email
from event import Event
from notificationmethod import NotificationMethod
from telegram import Telegram


class Reserve(Event):
    notificationmethod: NotificationMethod

    def __init__(self, notificationmethod: Email or Telegram):
        self.notificationmethod = notificationmethod

    def event(self):
        print("預約課程")
