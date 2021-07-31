from django.db import models

from apps.users.models import User

answer_choices = (
    ('yes', 'Да'),
    ('no', 'Нет'),
    ('sometimes', 'Иногда')
)


class Test(models.Model):
    question = models.CharField('Текст вопроса', max_length=150)
    answer = models.CharField(verbose_name='Ответы', max_length=20, choices=answer_choices)

    class Meta:
        verbose_name = 'Тестирование'
        verbose_name_plural = 'Тестирования'


class ResultTests(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.BooleanField('Результат', default=True)

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
