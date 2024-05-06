from self import self

import enus
from cancel import Cancel
from email import Email
from event import Event
from language_system import LanguageSystem
from notificationmethod import NotificationMethod
from reserve import Reserve
from user import User


class Student(User):
    event: Event

    def __init__(self, event: Reserve and Cancel):
        self.event = event

    def do(self):
        self.event.event()


stu = Student(Reserve(Email.notify(self)))
stu.do()
