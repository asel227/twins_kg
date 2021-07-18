import uuid

from django.db import models

from utils.uploads import upload_instance


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Picture(models.Model):
    image = models.ImageField(verbose_name='Изображение',
                              upload_to=upload_instance)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.id} - image'


class Audio(models.Model):
    file = models.FileField(verbose_name='Озвучка', blank=False, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = 'Аудио'
        verbose_name_plural = 'Аудио'

    def __str__(self):
        return self.file.name


class Card(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 related_name='cards',
                                 null=True)
    pictures = models.ManyToManyField(to=Picture, blank=True,
                                      related_name='cards_pictures')

    file = models.FileField(upload_to='audios/', null=True, verbose_name="Аудио")

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

    def __str__(self):
        return self.name

    @property
    def get_first_picture(self):
        return self.pictures.first()
