# Generated by Django 5.1.3 on 2024-12-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]