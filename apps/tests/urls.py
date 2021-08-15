from django.urls import path

from apps.tests.views import TestAPIView, ResultsAPIView, AnswerAPIView

urlpatterns = [
    path('tests/', TestAPIView.as_view(), name='api_tests'),
    path('answer/', AnswerAPIView.as_view(), name='api_answer'),
    path('results/', ResultsAPIView.as_view(), name='api_results'),
]