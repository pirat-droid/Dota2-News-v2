# Generated by Django 3.0.5 on 2020-05-09 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0021_auto_20200509_2131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentmodel',
            old_name='post_id',
            new_name='post',
        ),
    ]
