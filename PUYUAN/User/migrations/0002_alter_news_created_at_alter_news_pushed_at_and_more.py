# Generated by Django 4.2.5 on 2023-10-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='pushed_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
