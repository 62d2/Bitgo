from model.notification import Notification


class BaseNotice:
    """
    This will have all the system implemention for the notifiucation accoss all the clinet
    """

    def __init__(self, notification: Notification):
        self.notification = notification

    def send(self):
        """
        send the message using the client
        :return:
        """
        pass
