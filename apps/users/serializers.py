from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.validators import UniqueValidator

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
            'id', 'first_name', 'last_name', 'middle_name', 'age',
            'gender', 'phone_number', 'is_active', 'password'
        )


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'middle_name', 'age',
            'gender', 'phone_number'
        )


class RegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.IntegerField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'middle_name', 'age',
                  'gender', 'phone_number', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            last_name=validated_data['last_name'],
            first_name=validated_data['first_name'],
            middle_name=validated_data['middle_name'],
            age=validated_data['age'],
            gender=validated_data['gender'],
            phone_number=validated_data['phone_number'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

