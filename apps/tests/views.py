from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.tests.serializers import ResultTestsSerializer, TestSerializer
from apps.tests.models import Test, ResultTests


class TestAPIView(ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [AllowAny, ]


class ResultTestsAPIView(ListCreateAPIView):
    queryset = ResultTests.objects.all()
    serializer_class = ResultTestsSerializer
    permission_classes = [AllowAny, ]