from typing import List
from enus import Enus
from event import Event
from line import Line
from notificationmethod import NotificationMethod
from user import User


class Congratulate(Event):
    recipients = List

    def __init__(self):
        self.recipients = []

    def get_information(self, user: User):
        username: str = user.username
        sentence: str = user.language.get_sentence("congratulate")
        information = (username, sentence)
        self.recipients.append(information)  #recipients = [('one','新年快樂'),('two','Happy Chinese New Year')]



    def launch_event(self):
        """
        echo 所有username & 對應語系祝賀
        """
        for username, sentence in self.recipients:
            information: str = f"{username} {sentence} "
            for method in self.notification_method:
                method.notify(information)
