from notificationmethod import NotificationMethod


class Telegram(NotificationMethod):
    def notify(self, sentence: str):
        print("{} by Telegram".format(sentence))
