from django.urls import path

from apps.tests.views import TestAPIView

urlpatterns = [
    path('tests/', TestAPIView.as_view(), name='api_tests'),
]