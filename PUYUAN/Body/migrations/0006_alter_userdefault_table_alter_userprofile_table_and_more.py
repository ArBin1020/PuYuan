# Generated by Django 4.2.6 on 2023-10-19 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Body', '0005_alter_userdefault_table_alter_userprofile_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userdefault',
            table='Body_User_Default',
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='Body_User_Profile',
        ),
        migrations.AlterModelTable(
            name='usersetting',
            table='Body_User_Setting',
        ),
    ]
