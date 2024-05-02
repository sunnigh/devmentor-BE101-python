class Event:
    """
    關聯NotifycationMethod
    """

    def login(self):
        pass

    def reserve(self):
        pass

    def cancel(self):
        pass


class Login(Event):
    def login(self):
        pass


class Reserve(Event):
    def reserve(self):
        pass


class Cancel(Event):
    def cancel(self):
        pass


class NotifycationMethod:
    """
    關聯Event
    echo 不同方法出來
    """

    def notify(self):
        pass


class SMS(NotifycationMethod):
    def notify(self):
        pass


class Email(NotifycationMethod):
    def notify(self):
        pass


class Telegram(NotifycationMethod):
    def notify(self):
        pass
