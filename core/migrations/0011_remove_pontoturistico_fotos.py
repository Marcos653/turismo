# Generated by Django 4.0.3 on 2022-03-14 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_pontoturistico_fotos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pontoturistico',
            name='fotos',
        ),
    ]
