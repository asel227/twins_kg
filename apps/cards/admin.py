import django.contrib

from apps.cards.models import Category, Card


@django.contrib.admin.register(Category)
class CategoryAdmin(django.contrib.admin.ModelAdmin):
    list_display = ['name']


@django.contrib.admin.register(Card)
class CardAdmin(django.contrib.admin.ModelAdmin):
    list_display = ['name', 'description', 'category', 'pictures', 'file']
    # filter_horizontal = ['picture']
