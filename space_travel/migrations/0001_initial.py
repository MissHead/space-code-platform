# Generated by Django 3.2.4 on 2021-06-23 14:59

from django.db import migrations, models
import django.utils.timezone
import space_travel.helpers
import space_travel.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('payload', models.JSONField(default=dict)),
                ('origin_planet', models.CharField(max_length=70)),
                ('destination_planet', models.CharField(max_length=70)),
                ('value', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('disabled_at', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pilot_certification', models.CharField(max_length=7, validators=[space_travel.helpers.certification_validate])),
                ('name', models.CharField(max_length=70)),
                ('age', space_travel.models.IntegerRangeField()),
                ('credits', models.IntegerField(default=0)),
                ('location_planet', models.CharField(max_length=70)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('disabled_at', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('weight', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('disabled_at', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_capacity', models.IntegerField()),
                ('fuel_level', models.IntegerField()),
                ('weight_capacity', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('disabled_at', models.DateTimeField(default=None)),
            ],
        ),
    ]
