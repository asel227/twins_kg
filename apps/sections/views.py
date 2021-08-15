from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.sections.serializers import TimeTableSerializer, LogopedicSerializer, ExerciseSerializer, PuzzleSerializer
from apps.sections.models import TimeTableItem, Logopedic, Exercise, Puzzle


class TimeTableAPIView(ListCreateAPIView):
    queryset = TimeTableItem.objects.all()
    serializer_class = TimeTableSerializer
    permission_classes = [AllowAny, ]


class LogopedicAPIView(ListCreateAPIView):
    queryset = Logopedic.objects.all()
    serializer_class = LogopedicSerializer
    permission_classes = [AllowAny, ]
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        audio_files = LogopedicSerializer(data=request.data)
        if audio_files.is_valid():
            audio_files.save()
            return Response(audio_files.data, status=status.HTTP_201_CREATED)
        else:
            return Response(audio_files.errors, status=status.HTTP_400_BAD_REQUEST)


class ExerciseAPIView(ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class PuzzleAPIView(ListCreateAPIView):
    queryset = Puzzle.objects.all()
    serializer_class = PuzzleSerializer
