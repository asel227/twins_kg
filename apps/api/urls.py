from django.urls import path

from apps.api.views import (
    UsersListAPIView,UserAuthView,
    UserRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path('auth', UserAuthView.as_view(), name='auth'),
    path('users', UsersListAPIView.as_view(), name='users_list'),
    path('users/<int:pk>',
         UserRetrieveUpdateDestroyAPIView.as_view(), name='user_detail'),

]