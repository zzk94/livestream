# Generated by Django 2.1.dev20170216045417 on 2018-04-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livestream', '0002_auto_20180414_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='time',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]