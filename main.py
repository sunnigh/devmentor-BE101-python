# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


"""
object:user
attribute:username
method:
        1.選擇語系(User)
        2.註冊(User)
            NotifycationMethod:email & sms
        3.預約與取消(Student)
            NotifycationMethod:email & telegram
"""
import enus
from email import Email
from guest import Guest
from signup import Signup
from sms import Sms
from user import User
from zhtw import Zhtw

if __name__ == '__main__':
    # language = enus.Enus()
    # languagetw = Zhtw()
    # user = User("Alex", language)
    # user.do()

    signup = Signup()
    languagetw = Zhtw()

    signup.add_notification_method(Sms())
    # signup.add_notification_method(Email())
    signup.event(Guest('Jonny', languagetw))

# Press the green button in the gutter to run the script.
