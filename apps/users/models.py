from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


GENDER_CHOICES = (
    ('others', 'Другое'),
    ('male', 'Мужской'),
    ('female', 'Женский')
)


class UserManager(BaseUserManager):
    """
        This is a manager for Account class
    """

    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError("Users must have an phone_number")

        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(phone_number=phone_number,
                                password=password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
      Custom user class inheriting AbstractBaseUser class
    """
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    middle_name = models.CharField(verbose_name='Отчество',
                                   max_length=255,
                                   blank=True)
    age = models.CharField(verbose_name='Дата рождения', max_length=20)
    gender = models.CharField(verbose_name='Пол', max_length=20, choices=GENDER_CHOICES)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='Дата/время регистрации',
                                       auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Последний вход',
                                      auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.phone_number
