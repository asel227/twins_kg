from rest_framework.serializers import ModelSerializer

from apps.sections.models import TimeTableItem, Logopedic, Exercise, Puzzle


class TimeTableSerializer(ModelSerializer):
    class Meta:
        model = TimeTableItem
        fields = '__all__'


class LogopedicSerializer(ModelSerializer):
    class Meta:
        model = Logopedic
        fields = '__all__'


class ExerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class PuzzleSerializer(ModelSerializer):
    class Meta:
        model = Puzzle
        fields = '__all__'
