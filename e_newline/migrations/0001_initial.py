# Generated by Django 4.0.3 on 2023-09-23 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('video_id', models.CharField(blank=True, max_length=50, verbose_name='video_id')),
                ('level', models.CharField(choices=[('beg', 'beg'), ('imp', 'imp'), ('int', 'int')], max_length=3, verbose_name='level')),
                ('steps', models.URLField(blank=True, max_length=150, verbose_name='steps')),
            ],
        ),
    ]