# Generated by Django 3.0.5 on 2020-05-09 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0020_remove_commentmodel_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentmodel',
            old_name='post',
            new_name='post_id',
        ),
    ]
