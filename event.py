from abc import ABC, abstractmethod
from typing import List
from notificationmethod import NotificationMethod
from user import User


class Event(ABC):
    user: User
    notification_method: List[NotificationMethod] = []

    def __init__(self):
        self.notification_method = []

    def add_notification_method(self, notification_method: NotificationMethod):
        """
        將通知管道放入列表
        """
        self.notification_method.append(notification_method)

    @abstractmethod
    def launch(self, user: User):
        pass
