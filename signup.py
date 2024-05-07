from email import Email
from event import Event
from notificationmethod import NotificationMethod
from sms import Sms
from telegram import Telegram


class Signup(Event):
    notificationmethod: NotificationMethod


    def __init__(self, notificationmethod: Sms or Email):
        self.notificationmethod = notificationmethod

    def event(self):
        print('註冊')
