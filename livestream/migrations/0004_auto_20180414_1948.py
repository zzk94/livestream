# Generated by Django 2.1.dev20170216045417 on 2018-04-14 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livestream', '0003_auto_20180414_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
        ),
    ]
