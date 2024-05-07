from notificationmethod import NotificationMethod


class Telegram(NotificationMethod):
    def notify(self):
        print("by Telegram")
