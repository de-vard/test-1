# Generated by Django 4.1.4 on 2023-02-08 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('a', 'Легкий уровень'), ('b', 'Средний уровень'), ('c', 'Сложный уровень')], max_length=1, verbose_name='Уровень сложности'),
        ),
    ]
