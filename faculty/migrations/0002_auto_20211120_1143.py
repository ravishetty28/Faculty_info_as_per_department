# Generated by Django 3.1 on 2021-11-20 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name': 'faculty', 'verbose_name_plural': 'faculties'},
        ),
        migrations.RenameField(
            model_name='department',
            old_name='department_id',
            new_name='departmentId',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='department_name',
            new_name='departmentName',
        ),
        migrations.RenameField(
            model_name='faculty',
            old_name='date_of_joining',
            new_name='dateOfJoining',
        ),
        migrations.RenameField(
            model_name='faculty',
            old_name='faculty_name',
            new_name='facultyName',
        ),
    ]