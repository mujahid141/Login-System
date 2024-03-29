# Generated by Django 5.0 on 2024-02-03 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('major', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
