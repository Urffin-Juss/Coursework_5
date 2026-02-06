
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    telegram_id = serializers.IntegerField(read_only=True, required=True)
    email = serializers.EmailField(read_only=True,
                                   required=True,
                                   validators=[UniqueValidator(queryset=User.objects.all())]
                                   )

    username = serializers.CharField(read_only=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(read_only=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password2 = serializers.CharField(read_only=True, validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('telegram_id', 'username', 'email', 'password')


    def validate(self, attrs):
        if attrs['password'] !=['password2']:
            raise serializers.ValidationError('Passwords do not match')
        return attrs

    def create(self, validated_data):

        validated_data.pop('password2')

        user = User.objects.get(
            username=validated_data['username'],
            email=validated_data['email'],
            telegram_id=validated_data['telegram_id']
        )
        return user


