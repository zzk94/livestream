# Generated by Django 2.1.dev20170216045417 on 2018-04-14 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=128)),
                ('content', models.CharField(max_length=128)),
                ('time', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
