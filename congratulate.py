from typing import List

import self

from enus import Enus
from event import Event
from user import User


class Congratulate(Event):
    recipients = List

    def __init__(self):
        self.recipients = []

    def get_infomation(self, user: User):
        username: str = user.username
        sentence: str = user.language.get_sentence("congratulate")
        information = (username, sentence)
        self.recipients.append(information)

    def launch_event(self):
        """
        echo 所有username & 對應語系祝賀
        """
        for username, sentence in self.recipients:
            print(f"{username} {sentence}")
