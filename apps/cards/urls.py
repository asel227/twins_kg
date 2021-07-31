from django.urls import path

from apps.cards.views import CardListCreateAPIView, CardRetrieveUpdateDestroyAPIView, CardCreateAPIView

urlpatterns = [
    path('cards/',
         CardListCreateAPIView.as_view(), name='api_cards_list'),
    path('cards/<int:pk>',
         CardRetrieveUpdateDestroyAPIView.as_view(),
         name='api_cards_detail'),
    path('create_card', CardCreateAPIView.as_view(), name='api_card_create'),
]