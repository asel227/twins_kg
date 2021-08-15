from django.contrib import admin

from apps.tests.models import Test, Answer, Results


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'question']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['text', 'answer1', 'answer2', 'answer3']


@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ['test', 'user', 'score']

