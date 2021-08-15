from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.cards.models import Card, Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CardSerializer(ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        source='category',
        queryset=Category.objects.all()
    )
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Card
        fields = ('id', 'name', 'description', 'category_id',
                  'category', 'pictures', 'file')


class CardDetailSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'id', 'name', 'description', 'category_id',
            'category', 'pictures', 'file'
        )