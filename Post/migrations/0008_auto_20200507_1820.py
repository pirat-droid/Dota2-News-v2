# Generated by Django 3.0.5 on 2020-05-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0007_auto_20200507_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playermodel',
            name='photo',
            field=models.ImageField(upload_to='photo_player/', verbose_name='Фото игрока'),
        ),
    ]