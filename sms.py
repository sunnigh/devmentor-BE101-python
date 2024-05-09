from notificationmethod import NotificationMethod


class Sms(NotificationMethod):
    def notify(self, sentence: str):
        print("{} by SMS".format(sentence))
