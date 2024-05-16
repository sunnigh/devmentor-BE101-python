from abc import ABC, abstractmethod
from typing import List
from notificationmethod import NotificationMethod
from user import User


class Event(ABC):
    notification_method: List[NotificationMethod] = []

    def __init__(self):
        self.notification_method = []

    def add_notification_method(self, notification_method: NotificationMethod):
        """
        將通知管道放入列表
        """
        self.notification_method.append(notification_method)

    def launch(self, user: User):
        username: str = user.username
        sentence: str = user.language.get_sentence(self.launch_event())
        notify_sentence = "{} {}".format(username, sentence)
        for method in self.notification_method:
            method.notify(notify_sentence)

    @abstractmethod
    def launch_event(self):
        pass
