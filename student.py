from self import self
from cancel import Cancel
from email import Email
from event import Event
from reserve import Reserve
from user import User


class Student(User):
    event: Event

    def __init__(self):
        pass

    def do(self,event: Reserve or Cancel):
        event.event()


stu = Student()
stu.do(Reserve(Email().notify()))
