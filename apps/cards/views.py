import json

from django.http import JsonResponse
from django.views import View

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


#
#     def get(self, request, format=None):
#         photo = ImagesCliente.objects.all()
#         serializer = ImagesClienteSerializer(photo, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         serializer = ImagesClienteSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PhotoDetailView(APIView):
#
#     def get_object(self, pk):
#         try:
#             return ImagesCliente.objects.get(pk=pk)
#         except:
#             return Response(
#                 data={'error': 'Фотография не найдена'},
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#
#     def get(self, request, pk, format=None):
#         photo = self.get_object(pk)
#         serializer = ImagesClienteSerializer(photo, context={'request': request})
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         serializer = ImagesClienteSerializer(data=request.data, files=request.FILES)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         photo = self.get_object(pk)
#         photo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def put(self, request, pk, format=None):
#         photo = self.get_object(pk)
#         serializer = ImagesClienteSerializer(photo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.status.HTTP_400_BAD_REQUEST)
