from rest_framework import serializers
from users.models import Demo


class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields = "__all__"
