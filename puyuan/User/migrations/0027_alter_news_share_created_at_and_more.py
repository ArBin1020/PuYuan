# Generated by Django 4.2.6 on 2023-12-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0026_alter_news_share_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_share',
            name='created_at',
            field=models.CharField(default='2023-12-05 01:47:41', max_length=50),
        ),
        migrations.AlterField(
            model_name='news_share',
            name='pushed_at',
            field=models.CharField(default='2023-12-05 01:47:41', max_length=50),
        ),
        migrations.AlterField(
            model_name='news_share',
            name='updated_at',
            field=models.CharField(default='2023-12-05 01:47:41', max_length=50),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='created_at',
            field=models.CharField(default='2023-12-05 01:47:41', max_length=50),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='updated_at',
            field=models.CharField(default='2023-12-05 01:47:41', max_length=50),
        ),
    ]
