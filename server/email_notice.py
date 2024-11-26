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
        Implementatipon for the email based Noticaition
        :return:
        """
        pass

    def retry(self):
        pass
