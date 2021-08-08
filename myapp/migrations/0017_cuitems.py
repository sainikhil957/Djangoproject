# Generated by Django 3.2.2 on 2021-05-12 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_remove_fdform_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothname', models.CharField(default=None, max_length=100)),
                ('clothfile', models.ImageField(default='', upload_to='media/image')),
                ('clothtype', models.CharField(max_length=100)),
                ('clothcolour', models.CharField(max_length=100)),
                ('clothpattern', models.CharField(max_length=100)),
                ('clothsizes', models.CharField(max_length=100)),
                ('clothprice', models.CharField(default=None, max_length=100)),
                ('username', models.CharField(default=None, max_length=100)),
            ],
            options={
                'db_table': 'cuitems_table',
            },
        ),
    ]
