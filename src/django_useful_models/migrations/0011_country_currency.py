# Generated by Django 3.2 on 2021-05-04 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_useful_models', '0010_remove_country_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='currency',
            field=models.ManyToManyField(to='django_useful_models.Currency'),
        ),
    ]