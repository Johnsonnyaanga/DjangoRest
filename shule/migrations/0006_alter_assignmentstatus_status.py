# Generated by Django 4.0.1 on 2022-01-23 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shule', '0005_alter_assignment_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentstatus',
            name='status',
            field=models.CharField(choices=[('complete', 'complete'), ('incomplete', 'incomplete')], max_length=250, null=True),
        ),
    ]
