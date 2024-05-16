import unittest
from mock import MagicMock
from event import Event
from cancel import Cancel
from user import User
from notificationmethod import NotificationMethod


class TestCancelEvent(unittest.TestCase):
    def test_launch_event(self):
        # 創建一個模擬的User對象
        user = MagicMock(spec=User)
        user.username = 'JohnDoe'
        user.language.get_sentence.return_value = 'has cancelled the event.'

        # 創建一個模擬的NotificationMethod對象
        notification_method = MagicMock(spec=NotificationMethod)

        # 創建Cancel事件實例並添加通知方法
        event = Cancel()
        event.add_notification_method(notification_method)

        # 觸發事件
        event.launch(user)

        # 驗證是否調用了通知方法
        notification_method.notify.assert_called_once_with('JohnDoe has cancelled the event.')


if __name__ == '__main__':
    unittest.main()
