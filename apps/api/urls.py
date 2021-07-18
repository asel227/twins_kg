from django.urls import path

from apps.api.views import (
    UsersListAPIView, UserAuthView,
    UserRetrieveUpdateDestroyAPIView, CardListCreateAPIView, CardRetrieveUpdateDestroyAPIView, RegisterAPIView,
    TestAPIView, TimeTableAPIView,
    # AudioUploadView,
)

urlpatterns = [
    path('auth', UserAuthView.as_view(), name='auth'),
    path('users', UsersListAPIView.as_view(), name='users_list'),
    path('users/<int:pk>',
         UserRetrieveUpdateDestroyAPIView.as_view(), name='user_detail'),
    path('register', RegisterAPIView.as_view(), name='register'),
    path('cards',
         CardListCreateAPIView.as_view(), name='api_cards_list'),
    path('cards/<int:pk>',
         CardRetrieveUpdateDestroyAPIView.as_view(),
         name='api_card_detail'),
    path('tests', TestAPIView.as_view(), name='api_tests'),
    path('timetable', TimeTableAPIView.as_view(), name='api_time_table'),
    # path('api/files', AudioUploadView.as_view(), name='api_file'),
]