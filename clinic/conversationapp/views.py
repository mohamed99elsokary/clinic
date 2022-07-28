from datetime import datetime, timedelta

import pytz
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models, serializers


class ConversationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Conversation.objects.all()
    serializer_class = serializers.ConversationSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = serializers.ConversationDetailsSerializer
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.is_doctor == True:
            now = datetime.now(pytz.timezone("Africa/Cairo")) + timedelta(hours=2)
            self.queryset = models.Conversation.objects.filter(
                date=now,
                start_time__lte=now,
                is_closed=False,
            )
        else:
            self.queryset = models.Conversation.objects.filter(user=request.user)
        return super().list(request, *args, **kwargs)

    @action(
        methods=["get"],
        detail=True,
        url_path="close-conversations",
    )
    def close_conversation(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_closed = True
        instance.save()
        self.serializer_class = serializers.ConversationDetailsSerializer
        return super().retrieve(request, *args, **kwargs)


class MessageViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
