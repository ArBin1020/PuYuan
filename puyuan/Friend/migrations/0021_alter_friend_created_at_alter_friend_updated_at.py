# Generated by Django 4.2.6 on 2023-12-04 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Friend', '0020_alter_friend_created_at_alter_friend_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='created_at',
            field=models.DateTimeField(default='2023-12-04 19:42:32'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='updated_at',
            field=models.DateTimeField(default='2023-12-04 19:42:32'),
        ),
    ]