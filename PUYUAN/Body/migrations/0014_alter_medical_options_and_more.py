# Generated by Django 4.2.6 on 2023-11-17 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Body', '0013_alter_a1c_created_at_alter_a1c_recorded_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medical',
            options={},
        ),
        migrations.RenameField(
            model_name='medical',
            old_name='antu_hypertensive',
            new_name='anti_hypertensive',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='invite_code',
            field=models.IntegerField(default=1),
        ),
    ]
