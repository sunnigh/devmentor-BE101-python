from notificationmethod import NotificationMethod


class Email(NotificationMethod):

    def launch_method(self):
        # 執行寄送
        return "Email"
