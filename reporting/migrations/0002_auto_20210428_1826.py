# Generated by Django 3.2 on 2021-04-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cityweather',
            name='fetch_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='cityweather',
            name='sunrise',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='cityweather',
            name='sunset',
            field=models.DateTimeField(),
        ),
    ]
