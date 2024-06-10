import unittest
from fakenotify import FakeNotify
from signup import Signup
from cancel import Cancel
from guest import Guest
from student import Student
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

    def test_cancel_notification(self):
        fake_notify = FakeNotify()
        cancel = Cancel()
        cancel.add_notification_method(fake_notify)
        student = Student('Sam', Enus())
        cancel.launch(student)
        # Assert
        self.assertEqual(
            'Sam cancel successfully',
            fake_notify.expect_sentence
        )


if __name__ == '__main__':
    unittest.main()
