from rest_framework import serializers

from . import models


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="first_name")

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["user"] = request.user
        conversation = validated_data["conversation"]
        if conversation.is_closed == True:
            raise serializers.ValidationError(
                {"conversation": "this conversation is closed"}
            )
        return models.Message.objects.create(**validated_data)

    class Meta:
        model = models.Message
        fields = "__all__"


class ConversationSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="first_name")

    last_msg = serializers.SerializerMethodField()

    class Meta:
        model = models.Conversation
        fields = "__all__"

    def get_last_msg(self, obj):
        msg = models.Message.objects.filter(conversation=obj).last()
        serializer = MessageSerializer(msg)
        return serializer.data


class ConversationDetailsSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="first_name")
    messages = MessageSerializer(
        read_only=True, source="conversation_messages", many=True
    )

    class Meta:
        model = models.Conversation
        fields = "__all__"
