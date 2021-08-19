from django.db import models

from apps.users.models import User


class Test(models.Model):
    # name = models.CharField(verbose_name='Название', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=255)
    question = models.CharField(verbose_name='Текст вопроса', max_length=200)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Тестирование'
        verbose_name_plural = 'Тестирования'


class Answer(models.Model):
    text = models.ForeignKey(Test, verbose_name='Вопросы', on_delete=models.CASCADE)
    answer1 = models.BooleanField(verbose_name='Да', default=False)
    answer2 = models.BooleanField(verbose_name='Нет', default=False)
    answer3 = models.BooleanField(verbose_name='Иногда', default=False)

    def __str__(self):
        return f"question: {self.text.question}, answer1: {self.answer1}, answer2: {self.answer2}, answer3: {self.answer3}"

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Results(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.test)

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

