from event import Event
from guest import Guest


class Signup(Event):

    def launch(self, user: Guest):  # 依賴user
        """
        要求:
            echo 執行結果
            echo user name 資訊
            echo 的中區分出不同 Notification_method 訊息
        """
        username: str = user.username
        sentence: str = user.language.get_sentence('signup')
        notify_sentence = "{} {}".format(username, sentence)
        for method in self.notification_method:  # [Sms,Email]
            method.notify(notify_sentence)  # notify_sentence作為notify函數中的sentence傳入
