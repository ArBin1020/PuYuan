# Generated by Django 4.2.6 on 2023-11-17 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Body', '0015_rename_diabets_type_medical_diabetes_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medical',
            old_name='anti_hypertensive',
            new_name='anti_hypertensives',
        ),
    ]
