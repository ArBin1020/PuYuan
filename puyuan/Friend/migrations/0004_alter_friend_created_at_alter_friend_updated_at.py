# Generated by Django 4.2.7 on 2023-12-02 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Friend', '0003_rename_user_friend_user_id_alter_friend_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='created_at',
            field=models.DateTimeField(default='2023-12-03 02:45:06'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='updated_at',
            field=models.DateTimeField(default='2023-12-03 02:45:06'),
        ),
    ]