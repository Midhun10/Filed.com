# Generated by Django 3.1.4 on 2021-04-16 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='Song_Uploadtime',
        ),
    ]