from rest_framework.serializers import ModelSerializer

from apps.tests.models import Test, ResultTests


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class ResultTestsSerializer(ModelSerializer):
    class Meta:
        model = ResultTests
        fields = '__all__'