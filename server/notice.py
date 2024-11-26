from model.notification import Notification
from server import BaseCtx


class Notice(BaseCtx):
    """
    Notice can be medium with the notice object
    """

    def __init__(self, notification: Notification):
        self.notification = notification

    def pre_check_notification(self):
        pass

    def send_notification(self):
        pass

    def retry(self):
        pass
