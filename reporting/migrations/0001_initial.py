# Generated by Django 3.2 on 2021-04-28 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cityweather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fetch_date', models.DecimalField(decimal_places=2, max_digits=2)),
                ('sunrise', models.DecimalField(decimal_places=2, max_digits=2)),
                ('sunset', models.DecimalField(decimal_places=2, max_digits=2)),
                ('temp', models.DecimalField(decimal_places=2, max_digits=2)),
                ('feels', models.DecimalField(decimal_places=2, max_digits=2)),
                ('pressure', models.DecimalField(decimal_places=2, max_digits=2)),
                ('humidity', models.IntegerField()),
                ('dew_point', models.DecimalField(decimal_places=2, max_digits=2)),
                ('uvi', models.DecimalField(decimal_places=2, max_digits=2)),
                ('clouds', models.IntegerField()),
                ('wind_speed', models.DecimalField(decimal_places=2, max_digits=2)),
                ('wind_deg', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
            ],
            options={
                'unique_together': {('name', 'fetch_date')},
            },
        ),
    ]
