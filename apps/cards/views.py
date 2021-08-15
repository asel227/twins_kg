import json

from django.http import JsonResponse
from django.views import View
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.cards.serializers import CardSerializer, CardDetailSerializer
from apps.cards.models import Card


class CardView(View):

    def get_context_data(self, **kwargs):
        context = super(CardView, self).get_context_data(**kwargs)
        cards = context.get('card')
        context['first_picture'] = cards.get_first_picture

        return context

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode())

        cards = Card.objects.filter(id=data.get('card_id')).first()

        if cards is None:
            return JsonResponse({'detail': 'error'}, status=404)


class CardListCreateAPIView(ListCreateAPIView):
    queryset = Card.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CardSerializer


class CardRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CardDetailSerializer
