# Generated by Django 2.2 on 2021-07-11 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]