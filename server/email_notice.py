from model.email_notice_log import EmailNoticeLog
from server.base_notice import BaseNotice


class EmailNotice(BaseNotice):
    """ """

    @property
    def email_log(self):
        """
        if created take that from db
        :return:
        """
        return EmailNoticeLog()

    def send(self):
        """
        try sending the email notificaiton if it fails then retry
        and update the log with proper value
        :return:
        """
        pass
