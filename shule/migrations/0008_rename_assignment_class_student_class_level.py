# Generated by Django 4.0.1 on 2022-01-23 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shule', '0007_student_assignment_class'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='assignment_class',
            new_name='class_level',
        ),
    ]
