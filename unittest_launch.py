import unittest
from unittest.mock import Mock

from cancel import Cancel
from enus import Enus
from event import Event
from notificationmethod import NotificationMethod
from user import User


class TestEvent(unittest.TestCase):
    def test_launch(self):
        # 創建一個使用者和通知方法
        user = User("Alice", Enus())
        notification_method = Mock(spec=NotificationMethod)

        # 創建一個事件
        event = Cancel()
        event.add_notification_method(notification_method)

        # 模擬事件的啟動
        event.launch(user)

        # 確保通知方法被調用
        notification_method.notify.assert_called_once()


if __name__ == "__main__":
    unittest.main()
