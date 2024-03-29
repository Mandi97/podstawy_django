# Generated by Django 4.1.7 on 2023-02-15 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises_app', '0008_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='exercises_app.album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
