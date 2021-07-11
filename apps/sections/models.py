from django.db import models

from utils.uploads import upload_instance


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Test(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    middle_name = models.CharField(verbose_name='Отчество',
                                   max_length=255,
                                   blank=True)
    age = models.CharField(verbose_name='Дата рождения', max_length=20)
    gender = models.CharField(verbose_name='Пол', max_length=20)
    results = models.CharField(verbose_name='Результаты', max_length=20)

    class Meta:
        verbose_name = 'Тестирование'
        verbose_name_plural = 'Тестирования'


class Puzzle(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(
        verbose_name='Изображение', upload_to=upload_instance,
    )

    class Meta:
        verbose_name = 'Пазл'
        verbose_name_plural = 'Пазлы'

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    file = models.FileField(upload_to='videos/', null=True, verbose_name="Видео")

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'

    def __str__(self):
        return self.name


class TimeTable(models.Model):
    DAYS_OF_THE_WEEK = (
        ('1', 'Понедельник'),
        ('2', 'Вторник'),
        ('3', 'Среда'),
        ('4', 'Четверг'),
        ('5', 'Пятница'),
        ('6', 'Суббота'),
        ('7', 'Воскресеньe')
    )
    exercises = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    day = models.CharField(max_length=1, choices=DAYS_OF_THE_WEEK)

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


class TimeTableItem(models.Model):
    time_table = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    subject = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return 'Упражнение:{}, Время:{}-{}'.format(self.subject, self.start_time, self.end_time)

    class Meta:
        ordering = ('start_time',)
