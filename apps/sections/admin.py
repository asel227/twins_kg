from django.contrib import admin

from apps.sections import models
from apps.sections.models import Test, Picture, Card, Puzzle, Exercise, Category, TimeTable


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'middle_name', 'age',
                    'gender', 'results']


@admin.register(Picture)
class CardAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'file']


@admin.register(Puzzle)
class PuzzleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image']


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'file']


class TimeTableItemInline(admin.TabularInline):
    model = models.TimeTableItem
    raw_id_fields = ['subject']
    extra = 1


@admin.register(models.TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['exercises', 'day']
    inlines = [TimeTableItemInline]