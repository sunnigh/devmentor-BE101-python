import unittest

from fakenotify import FakeNotify
from notificationmethod import NotificationMethod
from signup import Signup
from cancel import Cancel
from guest import Guest
from student import Student
from sms import Sms
from email import Email
from enus import Enus
from zhtw import Zhtw


class TestEvent(unittest.TestCase):

    def test_signup_with_sms_notification(self):

        fake_notify = FakeNotify()
        signup = Signup()
        signup.add_notification_method(fake_notify)
        guest = Guest('Jonny', Zhtw())
        signup.launch(guest)

        self.assertEqual(
            "Jonny 註冊成功",
            fake_notify.expect_sentence
        )




    def test_signup_with_email_notification(self):
        signup = Signup()
        signup.add_notification_method(Email())
        guest = Guest('Jonny', Zhtw())
        signup.launch(guest)
        # Assert
        self.assertEqual('Jonny 註冊成功 by Email', 'Jonny 註冊成功 by SMS')

    def test_cancel_with_email_notification(self):
        cancel = Cancel()
        cancel.add_notification_method(Email())
        student = Student('Sam', Enus())
        cancel.launch(student)
        # Assert
        self.assertEqual('Sam cancel successfully by Email', 'Jonny cancel successfully by Email')


if __name__ == '__main__':
    unittest.main()
