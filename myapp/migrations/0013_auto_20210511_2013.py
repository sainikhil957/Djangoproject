# Generated by Django 3.2.2 on 2021-05-11 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20210511_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fdform',
            name='email',
        ),
        migrations.RemoveField(
            model_name='fdform',
            name='username',
        ),
    ]
