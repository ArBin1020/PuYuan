# Generated by Django 4.2.7 on 2023-12-02 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Body', '0007_alter_user_a1c_created_at_alter_user_a1c_recorded_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_a1c',
            name='created_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
        migrations.AlterField(
            model_name='user_a1c',
            name='recorded_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
        migrations.AlterField(
            model_name='user_a1c',
            name='updated_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
        migrations.AlterField(
            model_name='user_blood_pressure',
            name='recorded_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
        migrations.AlterField(
            model_name='user_blood_sugar',
            name='recorded_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
        migrations.AlterField(
            model_name='user_care',
            name='created_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
        migrations.AlterField(
            model_name='user_care',
            name='updated_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
        migrations.AlterField(
            model_name='user_default',
            name='created_at',
            field=models.CharField(default='2023-12-03 02:58:49:58:49', max_length=50),
        ),
        migrations.AlterField(
            model_name='user_default',
            name='updated_at',
            field=models.CharField(default='2023-12-03 02:58:49:58:49', max_length=50),
        ),
        migrations.AlterField(
            model_name='user_diary',
            name='recorded_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
        migrations.AlterField(
            model_name='user_drug',
            name='created_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
        migrations.AlterField(
            model_name='user_drug',
            name='recorded_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
        migrations.AlterField(
            model_name='user_drug',
            name='updated_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
        migrations.AlterField(
            model_name='user_medical',
            name='created_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
        migrations.AlterField(
            model_name='user_medical',
            name='updated_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
        migrations.AlterField(
            model_name='user_setting',
            name='created_at',
            field=models.CharField(default='2023-12-03 02:58:49:58:49', max_length=50),
        ),
        migrations.AlterField(
            model_name='user_setting',
            name='updated_at',
            field=models.CharField(default='2023-12-03 02:58:49:58:49', max_length=50),
        ),
        migrations.AlterField(
            model_name='user_vip',
            name='created_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
        migrations.AlterField(
            model_name='user_vip',
            name='ended_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
        migrations.AlterField(
            model_name='user_vip',
            name='started_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
        migrations.AlterField(
            model_name='user_vip',
            name='updated_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
        migrations.AlterField(
            model_name='user_weight',
            name='recorded_at',
            field=models.DateTimeField(default='2023-12-03 02:58:49'),
        ),
    ]
