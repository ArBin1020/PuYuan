# Generated by Django 4.2.6 on 2023-11-25 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Body', '0004_alter_userprofile_invite_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='invite_code',
            field=models.IntegerField(default=1),
        ),
    ]
