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


# from django.db import models
#
#
# class Test(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=500)
#     number_of_questions = models.IntegerField(default=1)
#
#     def __str__(self):
#         return self.name
#
#     def get_questions(self):
#         return self.question_set.all()
#
#
# class Question(models.Model):
#     title = models.CharField(max_length=200)
#     test = models.ForeignKey(Test, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
#     def get_answers(self):
#         return self.answer_set.all()
#
#
# class Answer(models.Model):
#     title = models.CharField(max_length=200)
#     correct = models.BooleanField(default=False)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"question: {self.question.title}, answer: {self.title}, correct: {self.correct}"
#
#
# class Results(models.Model):
#     test = models.ForeignKey(Test, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     score = models.FloatField()
#
#     def __str__(self):
#         return str(self.test)
#

# from django.template.defaultfilters import slugify
# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver
#
# class Test(models.Model):
#     name = models.CharField(max_length=1000)
#     questions_count = models.IntegerField(default=0)
#     description = models.CharField(max_length=70)
#     created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
#     slug = models.SlugField()
#     roll_out = models.BooleanField(default=False)
#
#     class Meta:
#         ordering = ['created']
#         verbose_name_plural = 'Тесты'
#
#     def __str__(self):
#         return self.name
#
#
# class Question(models.Model):
#     quiz = models.ForeignKey(Test, on_delete=models.CASCADE)
#     label = models.CharField(max_length=1000)
#     order = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.label
#
#
# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     text = models.CharField(max_length=1000)
#     is_correct = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.text
#
#
# class QuizTakers(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     quiz = models.ForeignKey(Test, on_delete=models.CASCADE)
#     correct_answers = models.IntegerField(default=0)
#     completed = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.user.username
#
#
# class Response(models.Model):
#     quiztaker = models.ForeignKey(QuizTakers, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer = models.ForeignKey(Answer,on_delete=models.CASCADE, null=True, blank=True)
#
#     def __str__(self):
#         return self.question.label
#
# @receiver(post_save, sender=Test)
# def set_default_quiz(sender, instance, created, **kwargs):
#     quiz = Test.objects.filter(id=instance.id)
#     quiz.update(questions_count=instance.question_set.filter(quiz=instance.pk).count())
#
#
# @receiver(post_save, sender=Question)
# def set_default(sender, instance, created, **kwargs):
#     quiz = Test.objects.filter(id=instance.quiz.id)
#     quiz.update(questions_count=instance.quiz.question_set.filter(quiz=instance.quiz.pk).count())
#
#
# @receiver(pre_save, sender=Test)
# def slugify_title(sender, instance, *args, **kwargs):
#     instance.slug = slugify(instance.name)