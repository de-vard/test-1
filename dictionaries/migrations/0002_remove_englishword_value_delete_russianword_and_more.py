# Generated by Django 4.1.4 on 2023-02-07 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='englishword',
            name='value',
        ),
        migrations.DeleteModel(
            name='RussianWord',
        ),
        migrations.AddField(
            model_name='englishword',
            name='value',
            field=models.CharField(default=2, max_length=75, verbose_name='Русское значение'),
            preserve_default=False,
        ),
    ]
