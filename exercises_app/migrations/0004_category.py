# Generated by Django 4.1.7 on 2023-02-15 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises_app', '0003_band_genre_band_still_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
