from rest_framework import serializers
from users.models import Demo, Te


class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields = "__all__"


class TeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Te
        fields = "__all__"
