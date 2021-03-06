# Generated by Django 2.0.13 on 2019-12-31 14:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0021_screeningmode'),
    ]

    operations = [
        migrations.AddField(
            model_name='screeningmode',
            name='x_resolution',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='screeningmode',
            name='y_resolution',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='screeningmode',
            unique_together={('image', 'user')},
        ),
    ]
