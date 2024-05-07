from notificationmethod import NotificationMethod


class Sms(NotificationMethod):
    def notify(self):
        print("by SMS")
