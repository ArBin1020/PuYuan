# Generated by Django 4.2.7 on 2023-12-03 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Friend', '0014_alter_friend_created_at_alter_friend_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='created_at',
            field=models.DateTimeField(default='2023-12-03 12:54:36'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='updated_at',
            field=models.DateTimeField(default='2023-12-03 12:54:36'),
        ),
    ]
