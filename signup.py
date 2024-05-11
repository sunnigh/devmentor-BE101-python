from typing import List
from event import Event
from guest import Guest
from notificationmethod import NotificationMethod
from user import User


class Signup(Event):
    notification_method: List[NotificationMethod] = []
    guest: Guest

    def __init__(self):
        self.notification_method = []

    def add_notification_method(self, notification_method: NotificationMethod):
        """
        將通知管道放入列表
        """
        self.notification_method.append(notification_method)

    def launch(self, guest: User):  # 依賴user
        """
        要求:
            echo 執行結果
            echo user name 資訊
            echo 的中區分出不同 Notification_method 訊息
        """
        username: str = guest.username
        sentence: str = guest.language.get_sentence('signup')
        notify_sentence = "{} {}".format(username, sentence)
        for method in self.notification_method:  # [Sms,Email]
            method.notify(notify_sentence)  # notify_sentence作為notify函數中的sentence傳入



