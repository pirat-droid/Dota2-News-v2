# Generated by Django 3.0.5 on 2020-05-10 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Post', '0022_auto_20200509_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='author',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='Commenter', to=settings.AUTH_USER_MODEL),
        ),
    ]
