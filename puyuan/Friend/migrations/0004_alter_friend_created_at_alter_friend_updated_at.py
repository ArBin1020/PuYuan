# Generated by Django 4.2.6 on 2023-12-10 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Friend', '0003_alter_friend_created_at_alter_friend_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='created_at',
            field=models.DateTimeField(default='2023-12-10 11:24:19'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='updated_at',
            field=models.DateTimeField(default='2023-12-10 11:24:19'),
        ),
    ]
