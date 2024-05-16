from event import Event


class Cancel(Event):

    def launch_event(self):
        return 'cancel'
