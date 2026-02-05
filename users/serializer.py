from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    telegram_id = serializers.IntegerField(read_only=True, required=True)

    class Meta:
        model = User
        fields = ('telegram_id', 'username', 'email', 'password')
