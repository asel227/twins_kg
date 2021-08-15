from django.urls import path

from apps.sections.views import TimeTableAPIView, LogopedicAPIView, ExerciseAPIView, PuzzleAPIView

urlpatterns = [
    path('timetable', TimeTableAPIView.as_view(), name='api_time_table'),
    path('logopedic', LogopedicAPIView.as_view(), name='api_logopedic'),
    path('exercise', ExerciseAPIView.as_view(), name='api_exercise'),
    path('Puzzle', PuzzleAPIView.as_view(), name='api_puzzle'),
]