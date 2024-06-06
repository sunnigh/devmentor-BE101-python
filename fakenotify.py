from notificationmethod import NotificationMethod


class FakeNotify(NotificationMethod):
    expect_sentence: str
    def launch_method(self):
        return ""

    def notify(self, sentence: str):
        self.expect_sentence = sentence