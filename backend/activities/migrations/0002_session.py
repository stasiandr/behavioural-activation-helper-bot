# Generated by Django 3.2.5 on 2021-07-13 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activities', models.ManyToManyField(to='activities.Activity')),
            ],
        ),
    ]