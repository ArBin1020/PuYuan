# Generated by Django 4.2.6 on 2023-12-04 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Friend', '0026_alter_friend_created_at_alter_friend_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='created_at',
            field=models.DateTimeField(default='2023-12-05 01:44:47'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='updated_at',
            field=models.DateTimeField(default='2023-12-05 01:44:47'),
        ),
    ]