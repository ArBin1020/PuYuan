# Generated by Django 4.2.5 on 2023-11-16 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Friend', '0002_alter_invite_invite_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='code',
        ),
        migrations.AlterField(
            model_name='friend',
            name='data_type',
            field=models.IntegerField(default=1, null=True),
        ),
    ]