# Generated by Django 4.2.19 on 2025-02-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, verbose_name='Владелец')),
                ('square', models.IntegerField(verbose_name='Сколько кв метров ')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('street', models.CharField(max_length=50, verbose_name='Улица')),
                ('year', models.DateTimeField(verbose_name='год постройки')),
                ('title', models.CharField(max_length=255)),
                ('property_type', models.CharField(choices=[('apartment', 'Квартира'), ('house', 'Дом')], default='apartment', max_length=20)),
            ],
        ),
    ]
