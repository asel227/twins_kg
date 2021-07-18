# Generated by Django 2.2 on 2021-07-18 16:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='audio',
        ),
        migrations.AddField(
            model_name='audio',
            name='file',
            field=models.FileField(null=True, upload_to='', verbose_name='Озвучка'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]