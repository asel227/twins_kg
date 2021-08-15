from django.db import models

from utils.uploads import upload_instance


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 related_name='cards',
                                 null=True)
    pictures = models.ImageField(upload_to=upload_instance, null=True, verbose_name="Картинки")
    file = models.FileField(upload_to=upload_instance, null=True, verbose_name="Аудио")

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

    def __str__(self):
        return self.name