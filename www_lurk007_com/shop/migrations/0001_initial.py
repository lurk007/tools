# Generated by Django 2.2 on 2021-02-11 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(default='', max_length=32)),
                ('uid_card', models.CharField(default='', max_length=24)),
                ('login_name', models.CharField(default='', max_length=24)),
                ('phone', models.CharField(default='', max_length=16)),
                ('email', models.CharField(default='', max_length=80)),
                ('power', models.CharField(default=2, max_length=1)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
