from notificationmethod import NotificationMethod


class Email(NotificationMethod):
    def notify(self):
        print("by Email")
