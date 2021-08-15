from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.tests.models import Test, Results, Answer


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class AnswerSerializer(ModelSerializer):
    questions = TestSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'


class ResultsSerializer(ModelSerializer):
    class Meta:
        model = Results
        fields = '__all__'
