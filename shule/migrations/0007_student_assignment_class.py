# Generated by Django 4.0.1 on 2022-01-23 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shule', '0006_alter_assignmentstatus_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='assignment_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shule.classlevel'),
        ),
    ]
