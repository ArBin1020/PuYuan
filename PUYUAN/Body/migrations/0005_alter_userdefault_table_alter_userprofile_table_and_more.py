# Generated by Django 4.2.6 on 2023-10-19 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Body', '0004_userdefault_alter_usersetting_options_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userdefault',
            table='Body_user_default',
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='Body_user_profile',
        ),
        migrations.AlterModelTable(
            name='usersetting',
            table='Body_user_setting',
        ),
    ]
