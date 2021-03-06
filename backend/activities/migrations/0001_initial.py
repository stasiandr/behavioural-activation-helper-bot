# Generated by Django 3.2.5 on 2021-07-13 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, verbose_name='first name')),
                ('type', models.CharField(choices=[('ST', 'Start'), ('EN', 'End'), ('NO', 'Normal')], default='NO', max_length=2)),
                ('end_date', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(default=5)),
            ],
        ),
    ]
