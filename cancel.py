from event import Event
from notificationmethod import NotificationMethod



class Cancel(Event):
    class Signup(Event):
        notificationmethod: NotificationMethod

        def __init__(self, notificationmethod: NotificationMethod):
            self.notificationmethod = notificationmethod

    def event(self):
        pass
