from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer, LoginSerializer
from .models import User
from django.contrib.auth import authenticate


class RegisterView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class loginView(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticad(
            username=serializer.validated_date["username"],
            password=serializer.validated_data["password"],
        )

        if not user:
            return Response(
                {"detail": "invalid credentials"}, status.HTTP_403_FORBIDDEN
            )

        return Response({"msg": f"Bem vindo"})
