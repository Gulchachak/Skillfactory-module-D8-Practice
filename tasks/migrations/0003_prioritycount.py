# Generated by Django 2.2.6 on 2020-05-07 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20191204_0703'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriorityCount',
            fields=[
                ('name', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
