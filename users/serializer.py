from attr.setters import validate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    telegram_id = serializers.IntegerField( required=True)
    email = serializers.EmailField(
                                   required=True,
                                   validators=[UniqueValidator(queryset=User.objects.all())]
                                   )

    #username = serializers.CharField(read_only=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])


    class Meta:
        model = User
        fields = '__all__'





    def create(self, validated_data):

        user = User.objects.create_user(**validated_data)

        return user


