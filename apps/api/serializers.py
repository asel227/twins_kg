from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from apps.cards.models import Card, Picture, Category
from apps.users.models import User


class AuthSerializer(Serializer):
    phone_number = serializers.CharField(max_length=60)
    password = serializers.CharField(max_length=128)


class UsersListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'middle_name', 'age',
            'gender', 'phone_number', 'is_active',
        )


class UsersCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'middle_name',
            'age', 'gender', 'phone_number',
            'is_active', 'password'
        )


class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'middle_name',
            'age', 'gender', 'phone_number',
        )


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class PictureSerializer(ModelSerializer):

    class Meta:
        model = Picture
        fields = '__all__'


class CardSerializer(ModelSerializer):
    card_id = serializers.PrimaryKeyRelatedField(
        source='card',
        queryset=Category.objects.all()
    )
    category = CategorySerializer(read_only=True)
    pictures = PictureSerializer(read_only=True, many=True)

    class Meta:
        model = Card
        fields = ('id', 'name', 'description', 'category_id',
                  'category', 'pictures', 'file')


class RegisterSerializer(ModelSerializer):
    phone_number = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')