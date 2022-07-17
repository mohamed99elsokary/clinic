from django.db import models
from django.db.models.signals import post_save

from clinic.notificationsapp.utils import send_notifications_to_users


class Notification(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True, default=None)
    date = models.DateField()
    url = models.URLField(max_length=200, null=True, blank=True, default=None)
    service = models.ForeignKey(
        "servicesapp.Service",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    article = models.ForeignKey(
        "articlesapp.Article",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )


def my_signal_name(sender, instance, **kwargs):
    send_notifications_to_users(instance)


post_save.connect(my_signal_name, sender=Notification)
