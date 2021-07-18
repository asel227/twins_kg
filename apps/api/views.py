from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.serializers import (
    AuthSerializer, UsersListSerializer,
    CardSerializer, RegisterSerializer, TestSerializer,
    TimeTableSerializer,
    # AudioSerializer,
)
from apps.cards.models import Card
from apps.sections.models import TimeTableItem
from apps.tests.models import Test
from apps.users.models import User


class UserAuthView(APIView):
    permission_classes = [AllowAny]
    serializer_class = AuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.filter(phone_number=serializer.data.get('phone_number')).first()

        if user is None:
            return Response(
                data={'error': 'Пользотеватель не найден'},
                status=status.HTTP_404_NOT_FOUND,
            )

        if not user.check_password(serializer.data.get('password')):
            return Response(
                data={'error': 'Не верный пароль'},
                status=status.HTTP_404_NOT_FOUND,
            )

        user_token, created = Token.objects.get_or_create(user=user)

        return Response(data={'token': user_token.key}, status=status.HTTP_200_OK)


class UsersListAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.filter(is_active=True)

    def get(self, request, *args, **kwargs):
        self.serializer_class = UsersListSerializer
        return super(UsersListAPIView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.serializer_class = UsersListSerializer
        return super(UsersListAPIView, self).post(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(serializer.validated_data.get('password'))
        instance.save()


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UsersListSerializer

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class CardListCreateAPIView(ListCreateAPIView):
    queryset = Card.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CardSerializer


class CardRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


# class AudioUploadView(APIView):
#     permission_classes = []
#     parser_class = (FileUploadParser,)
#
#     def post(self, request, *args, **kwargs):
#         file_serializer = AudioSerializer(data=request.data)
#
#         if file_serializer.is_valid():
#             file_serializer.save()
#             return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestAPIView(ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TimeTableAPIView(ListCreateAPIView):
    queryset = TimeTableItem.objects.all()
    serializer_class = TimeTableSerializer
