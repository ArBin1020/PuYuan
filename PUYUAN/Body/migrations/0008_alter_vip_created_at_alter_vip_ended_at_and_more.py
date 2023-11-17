# Generated by Django 4.2.5 on 2023-11-15 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Body', '0007_remove_unread_records_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vip',
            name='created_at',
            field=models.DateTimeField(default='2020-01-01 00:00:00'),
        ),
        migrations.AlterField(
            model_name='vip',
            name='ended_at',
            field=models.DateTimeField(default='2025-01-01 00:00:00'),
        ),
        migrations.AlterField(
            model_name='vip',
            name='started_at',
            field=models.CharField(default='2020-01-01 00:00:00', max_length=50),
        ),
        migrations.AlterField(
            model_name='vip',
            name='updated_at',
            field=models.DateTimeField(default='2020-01-01 00:00:00'),
        ),
    ]