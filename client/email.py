## class should be singleton


class EmailClient:
    def __class__(cls):
        if not cls.cli:
            cls.cli = EmailClient()

    def send_email(self, from_e, to_e, subject, content):
        pass
