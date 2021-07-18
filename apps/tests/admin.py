from django.contrib import admin

from apps.tests.models import Test, ResultTests


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']


@admin.register(ResultTests)
class ResultTestsAdmin(admin.ModelAdmin):
    list_display = ['test', 'user', 'result']

