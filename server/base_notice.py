from model.notification import Notification


class BaseNotice:
    """
    This will have all the system implementation for the notification access all the client
    """

    def __init__(self, notification: Notification):
        self.notification = notification

    def status(self):
        """
        check the status of the notification
        :return:
        """
        pass

    def send(self):
        """
        send the message using the client
        :return:
        """
        pass
