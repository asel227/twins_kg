from django.contrib import admin

from apps.cards.models import Category, Picture, Audio, Card


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Picture)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(Audio)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['audio']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'category', 'file']
