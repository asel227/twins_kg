from django.contrib import admin

from apps.cards.models import Category, Audio, Card


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


# @admin.register(Picture)
# class PictureAdmin(admin.ModelAdmin):
#     list_display = ['image']


@admin.register(Audio)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['file', 'id']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'category', 'pictures', 'file']
    # filter_horizontal = ['picture']
