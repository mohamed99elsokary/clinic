from rest_framework import mixins, viewsets

from . import models, serializers


class ConversationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Conversation.objects.all()
    serializer_class = serializers.ConversationSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = serializers.ConversationDetailsSerializer
        return super().retrieve(request, *args, **kwargs)


class MessageViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
