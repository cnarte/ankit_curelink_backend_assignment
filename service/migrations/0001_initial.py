# Generated by Django 4.0.4 on 2022-05-05 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contentandtimeperTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=150)),
                ('content_text', models.TextField()),
                ('publish_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='userandtopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('topic', models.CharField(max_length=150)),
                ('user_mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
