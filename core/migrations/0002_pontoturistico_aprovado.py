# Generated by Django 4.0.3 on 2022-03-12 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='aprovado',
            field=models.BooleanField(default=False),
        ),
    ]
