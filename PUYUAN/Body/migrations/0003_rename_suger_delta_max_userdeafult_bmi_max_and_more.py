# Generated by Django 4.2.6 on 2023-10-19 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Body', '0002_userdeafult'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdeafult',
            old_name='suger_delta_max',
            new_name='bmi_max',
        ),
        migrations.RenameField(
            model_name='userdeafult',
            old_name='user_id',
            new_name='diastolic_max',
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='bmi_min',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='body_fat_max',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='body_fat_min',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='diastolic_min',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='pulse_max',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='pulse_min',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='sugar_after_max',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='sugar_after_min',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='sugar_before_max',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='sugar_before_min',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='sugar_delta_max',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='sugar_delta_min',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='sugar_evening_max',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='sugar_evening_min',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='sugar_morning_max',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='sugar_morning_min',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='systolic_max',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='systolic_min',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='weight_max',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdeafult',
            name='weight_min',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('after_recording', models.BooleanField()),
                ('no_recording_for_a_day', models.BooleanField()),
                ('over_max_or_under_min', models.BooleanField()),
                ('after_meal', models.BooleanField()),
                ('unit_of_sugar', models.BooleanField()),
                ('unit_of_weight', models.BooleanField()),
                ('unit_of_height', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]