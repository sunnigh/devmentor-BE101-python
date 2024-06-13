from typing import List
from enus import Enus
from event import Event
from line import Line
from notificationmethod import NotificationMethod
from user import User


class Congratulate(Event):

    def launch_event(self):
        return 'congratulate'

