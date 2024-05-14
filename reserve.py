from event import Event
from student import Student


class Reserve(Event):

    def launch(self, user: Student):
        username: str = user.username
        sentence: str = user.language.get_sentence('reserve')
        notify_sentence = "{} {}".format(username, sentence)
        for method in self.notification_method:
            method.notify(notify_sentence)
