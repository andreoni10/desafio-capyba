# Generated by Django 4.0.4 on 2022-05-13 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_name', models.CharField(max_length=200)),
                ('film_release', models.IntegerField()),
                ('film_genre', models.CharField(max_length=200)),
            ],
        ),
    ]
