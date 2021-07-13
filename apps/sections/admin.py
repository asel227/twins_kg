from django.contrib import admin

from apps.sections import models
from apps.sections.models import Test, Puzzle, Exercise, Category, TimeTable


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'middle_name', 'age',
                    'gender', 'results']


@admin.register(Puzzle)
class PuzzleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image']


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'file']


class TimeTableItemInline(admin.TabularInline):
    model = models.TimeTableItem
    raw_id_fields = ['subject']
    extra = 3


@admin.register(models.TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['exercises', 'day']
    inlines = [TimeTableItemInline]