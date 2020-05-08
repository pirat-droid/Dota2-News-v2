# Generated by Django 3.0.5 on 2020-05-08 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0010_videomodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChanelModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название канала')),
                ('logo', models.ImageField(upload_to='chanel/logo', verbose_name='Логотип канала')),
            ],
            options={
                'verbose_name': 'Канал',
                'verbose_name_plural': 'Каналы',
            },
        ),
        migrations.AddField(
            model_name='videomodel',
            name='chanel',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='Post.ChanelModel', verbose_name='Канал'),
        ),
    ]
