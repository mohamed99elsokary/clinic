from clinic.notificationsapp.FCMManager import sendPush
from clinic.userapp.models import FcmToken


def send_notifications_to_users(notification):
    """
    get the notification object
    get the users fcm tokens
    send the tokens and the notification details to google
    """
    notification_title = notification.title
    tokens = list(FcmToken.objects.values_list("token", flat=True).distinct())
    dataObject = None
    sendPush(
        title=notification.title,
        msg=notification.description,
        registration_token=tokens,
        dataObject=dataObject,
    )
