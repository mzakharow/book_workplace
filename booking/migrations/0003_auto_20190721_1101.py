# Generated by Django 2.2.3 on 2019-07-21 11:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20190716_2001'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-day']},
        ),
        migrations.AddField(
            model_name='booking',
            name='free_places',
            field=models.PositiveIntegerField(blank=True, default=14, validators=[django.core.validators.MaxValueValidator(14)]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
