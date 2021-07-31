import json

from django.http import JsonResponse
from django.views import View
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.serializers import CardSerializer, CardDetailSerializer
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
    permission_classes = (IsAuthenticated,)
    serializer_class = CardSerializer


class CardRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CardDetailSerializer


class CardCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Card.objects.all()
    serializer_class = CardSerializer


# class FileUploadView(APIView):
#     permission_classes = [IsAuthenticated, ]
#     parser_class = (FileUploadParser,)
#
#     def post(self, request, *args, **kwargs):
#         file_serializer = FileSerializer(data=request.data)
#         if file_serializer.is_valid():
#             file_serializer.save()
#             return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)