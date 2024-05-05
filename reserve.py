from email import Email
from event import Event
from telegram import Telegram


class Reserve(Event):
    email: Email
    telegram: Telegram

    def __init__(self, email: Email, telegram: Telegram):
        self.email = email
        self.telegram = telegram

    def event(self):
        pass
