from model.notification import Notification


class NotificationService:
    def create(self, notification_meta) -> Notification:
        """
        create notification into the system and return the id of the notification

        :param notification_meta:
        :return:
        """
        # return Notification()

    def list(self) -> list[Notification]:
        """
        list all the notification in the system
        :return:
        """
        # return [Notification()]

    def delete(self, notification_id: int) -> Notification:
        """
        delete the notification from the system
        :param notification_id:
        :return:
        """
        # return Notification()

    def get(self, notification_id: int) -> Notification:
        """
        get the notification from the system
        :param notification_id:
        :return:
        """
        # return Notification()

    def send(self, notification_id: int) -> Notification:
        """
        identify the notification and it mode of delivery and send the notification
        :param notification_id:
        :return:
        """
        pass
