from rest_framework import serializers
from . import models


class field(serializers.ModelSerializer):
    class Meta:
        model = models.Field
        fields = "__all__"


class scientific_degree(serializers.ModelSerializer):
    class Meta:
        model = models.ScientificDegree
        fields = "__all__"


class experience(serializers.ModelSerializer):
    class Meta:
        model = models.Experience
        fields = "__all__"


class skill(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = "__all__"


class other(serializers.ModelSerializer):
    class Meta:
        model = models.Other
        fields = "__all__"


class cv(serializers.ModelSerializer):
    fields = field(many=True, read_only=True)
    scientific_degrees = scientific_degree(many=True, read_only=True)
    experiences = experience(many=True, read_only=True)
    skills = skill(many=True, read_only=True)
    others = other(many=True, read_only=True)

    class Meta:
        model = models.cv

        exclude = (
            "id",
            "name",
        )
