# Generated by Django 3.0.5 on 2020-05-08 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0017_auto_20200508_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videomodel',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Post.GameModel', verbose_name='Игра'),
        ),
        migrations.AlterField(
            model_name='videomodel',
            name='tournament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Post.TournamentModel', verbose_name='Турнир'),
        ),
    ]
