# Generated by Django 2.2.6 on 2020-05-07 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_prioritycount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prioritycount',
            old_name='count',
            new_name='todos_count',
        ),
    ]