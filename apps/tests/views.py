from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.tests.serializers import ResultsSerializer, TestSerializer, AnswerSerializer
from apps.tests.models import Test, Results, Answer


class TestAPIView(ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [AllowAny, ]


class AnswerAPIView(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [AllowAny, ]


class ResultsAPIView(ListAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer
    permission_classes = [IsAuthenticated, ]