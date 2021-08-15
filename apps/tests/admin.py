from django.contrib import admin

from apps.tests.models import Test, ResultTests


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']


@admin.register(ResultTests)
class ResultTestsAdmin(admin.ModelAdmin):
    list_display = ['test', 'user', 'result']


# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver
# from django.utils.text import slugify

# from apps.tests.models import Test, Question, Answer, Results
#
#
# @admin.register(Test)
# class TestAdmin(admin.ModelAdmin):
#     list_display = ['name', 'description', 'number_of_questions']
#
#
# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ['title', 'test']
#
#
# @admin.register(Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ['title', 'correct', 'question']
#
#
# @admin.register(Results)
# class ResultsAdmin(admin.ModelAdmin):
#     list_display = ['test', 'user', 'score']

