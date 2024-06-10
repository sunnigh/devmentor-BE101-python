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
from cancel import Cancel
from congratulate import Congratulate
from email import Email
from enus import Enus
from guest import Guest
from line import Line
from signup import Signup
from sms import Sms
from student import Student
from user import User
from zhtw import Zhtw

if __name__ == '__main__':
    # language = enus.Enus()
    # languagetw = Zhtw()
    # user = User("Alex", language)
    # user.do()

    signup = Signup()
    cancel = Cancel()
    languagetw = Zhtw()
    languageen = Enus()
    congra = Congratulate()

    signup.add_notification_method(Sms())
    signup.add_notification_method(Email())
    signup.launch(Guest('Jonny', languagetw))
    cancel.add_notification_method(Email())
    cancel.launch(Student('Sam', languageen))

    congra.add_notification_method(Line())
    user = User("one", Enus())
    user2 = User("two", Zhtw())
    congra.launch(user)
    congra.launch(user2)


# Press the green button in the gutter to run the script.
