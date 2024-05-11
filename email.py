from notificationmethod import NotificationMethod


class Email(NotificationMethod):
    def notify(self, sentence: str):
        print("{} by Email".format(sentence))
