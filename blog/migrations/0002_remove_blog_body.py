# Generated by Django 2.2.17 on 2020-12-18 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='body',
        ),
    ]
