# Generated by Django 5.0.4 on 2024-05-06 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('IT', 'InformationTechnology'), ('CE', 'ComputerEngineering')], default='InformationTechnology', max_length=2),
        ),
    ]
