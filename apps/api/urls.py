from django.urls import path

from apps.api.views import (
    UsersListAPIView, UserAuthView,
    UserRetrieveUpdateDestroyAPIView, CardListCreateAPIView, CardRetrieveUpdateDestroyAPIView, ExampleAPI,
)


urlpatterns = [
    path('auth', UserAuthView.as_view(), name='auth'),
    path('users', UsersListAPIView.as_view(), name='users_list'),
    path('users/<int:pk>',
         UserRetrieveUpdateDestroyAPIView.as_view(), name='user_detail'),
    path('cards/',
         CardListCreateAPIView.as_view(), name='api_cards_list'),
    path('cards/<int:pk>',
         CardRetrieveUpdateDestroyAPIView.as_view(),
         name='api_card_detail'),
    path('example-api', ExampleAPI.as_view(), name='example'),
]