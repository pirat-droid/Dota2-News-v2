# Generated by Django 3.0.5 on 2020-05-08 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0013_videomodel_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videomodel',
            name='link',
            field=models.CharField(max_length=150, verbose_name='Ссылка на видео'),
        ),
    ]
