# Generated by Django 4.2.6 on 2023-12-05 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Friend', '0028_alter_friend_created_at_alter_friend_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='created_at',
            field=models.DateTimeField(default='2023-12-06 00:23:11'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='updated_at',
            field=models.DateTimeField(default='2023-12-06 00:23:11'),
        ),
    ]
