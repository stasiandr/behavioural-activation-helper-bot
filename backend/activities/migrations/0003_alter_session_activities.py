# Generated by Django 3.2.5 on 2021-07-13 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='activities',
            field=models.ManyToManyField(blank=True, to='activities.Activity'),
        ),
    ]
