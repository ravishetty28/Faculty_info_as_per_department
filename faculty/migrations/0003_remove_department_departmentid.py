# Generated by Django 3.1 on 2021-11-20 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0002_auto_20211120_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='departmentId',
        ),
    ]