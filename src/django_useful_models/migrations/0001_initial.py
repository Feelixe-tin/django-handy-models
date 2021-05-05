# Generated by Django 3.2 on 2021-05-04 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_endonym', models.CharField(max_length=255, unique=True)),
                ('name_exonym', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'continents',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('symbol', models.CharField(blank=True, max_length=3, null=True)),
                ('iso_4217', models.CharField(blank=True, max_length=10, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'currencies',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_exonym', models.CharField(max_length=255, unique=True)),
                ('name_endonym', models.CharField(max_length=255)),
                ('capital_exonym', models.CharField(max_length=255)),
                ('capital_endonym', models.CharField(max_length=255)),
                ('calling_code', models.IntegerField(max_length=4, unique=True)),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_useful_models.continent')),
            ],
            options={
                'verbose_name_plural': 'contries',
            },
        ),
    ]