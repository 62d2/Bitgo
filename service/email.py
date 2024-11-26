from model.email_notice_log import EmailNoticeLog
from model.notification import Notification


class NotificationService:
    def send(self, notification: Notification) -> EmailNoticeLog:
        """
        create notification into the system and return the id of the notification

        :param notification:
        :return: EmailNoticeLog
        """
        # return EmailNoticeLog()
