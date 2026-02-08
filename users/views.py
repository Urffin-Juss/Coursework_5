from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import UserSerializer


class RegisterView(APIView):
    """Представление для регистрации"""

    @swagger_auto_schema(
        operation_description="Регистрация",
        operation_summary="Регистрация нового пользователя",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING, description="Почта"),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Пароль"
                ),
                "confirm_password": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Подтверждение пароля"
                ),
            },
            required=["email", "password", "confirm_password"],
        ),
        responses={
            201: openapi.Response(description="1"),
            400: "Ошибка валидации данных",
        },
        tags=["register"],
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)