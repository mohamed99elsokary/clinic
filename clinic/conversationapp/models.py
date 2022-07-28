from django.db import models

from clinic.reservationsapp.models import Reservation
from clinic.userapp.models import User

# Create your models here.


class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_chat")
    reservation = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    is_closed = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True, default=None)
    start_time = models.TimeField(null=True, blank=True, default=None)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    # relations
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="conversation_messages",
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    # fields
    message = models.TextField()
    attachment = models.FileField(upload_to="conversation", null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
