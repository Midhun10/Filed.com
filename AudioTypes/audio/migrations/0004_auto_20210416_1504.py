# Generated by Django 3.1.4 on 2021-04-16 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0003_auto_20210416_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='Song_Uploaddate',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='song',
            name='Song_Uploadtime',
            field=models.TimeField(default=None),
        ),
    ]
