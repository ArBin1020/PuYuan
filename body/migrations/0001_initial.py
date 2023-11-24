# Generated by Django 4.2.5 on 2023-10-14 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDefault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sugar_delta_max', models.FloatField(default=10.0)),
                ('sugar_delta_min', models.FloatField(default=1.0)),
                ('sugar_morning_max', models.FloatField(default=10.0)),
                ('sugar_morning_min', models.FloatField(default=1.0)),
                ('sugar_evening_max', models.FloatField(default=10.0)),
                ('sugar_evening_min', models.FloatField(default=1.0)),
                ('sugar_before_max', models.FloatField(default=10.0)),
                ('sugar_before_min', models.FloatField(default=1.0)),
                ('sugar_after_max', models.FloatField(default=10.0)),
                ('sugar_after_min', models.FloatField(default=1.0)),
                ('systolic_max', models.IntegerField(default=10)),
                ('systolic_min', models.IntegerField(default=1)),
                ('diastolic_max', models.IntegerField(default=10)),
                ('diastolic_min', models.IntegerField(default=1)),
                ('pulse_max', models.IntegerField(default=10)),
                ('pulse_min', models.IntegerField(default=1)),
                ('weight_max', models.FloatField(default=10.0)),
                ('weight_min', models.FloatField(default=1.0)),
                ('bmi_max', models.FloatField(default=10.0)),
                ('bmi_min', models.FloatField(default=1.0)),
                ('body_fat_max', models.FloatField(default=10.0)),
                ('body_fat_min', models.FloatField(default=1.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserWeight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('body_fat', models.FloatField()),
                ('bmi', models.FloatField()),
                ('recorded_at', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('after_recording', models.BooleanField(default=False)),
                ('no_recording_for_a_day', models.BooleanField(default=False)),
                ('over_max_or_under_min', models.BooleanField(default=True)),
                ('after_meal', models.BooleanField(default=True)),
                ('unit_of_sugar', models.BooleanField(default=True)),
                ('unit_of_weight', models.BooleanField(default=True)),
                ('unit_of_height', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.CharField(max_length=50)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('gender', models.BooleanField()),
                ('fcm_id', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('default', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='body.userdefault')),
                ('setting', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='body.usersetting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserMedical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diabetes_type', models.IntegerField()),
                ('oad', models.BooleanField()),
                ('insulin', models.BooleanField()),
                ('anti_hypertensives', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDrugUsed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('recorded_at', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDiet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('meal', models.IntegerField()),
                ('tag', models.CharField(max_length=200)),
                ('image', models.IntegerField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('recorded_at', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.IntegerField(default=1)),
                ('reply_id', models.IntegerField(default=1)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserA1c',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a1c', models.IntegerField()),
                ('recorded_at', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BloodSugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sugar', models.FloatField()),
                ('timeperiod', models.IntegerField()),
                ('recorded_at', models.CharField(max_length=50)),
                ('drug', models.IntegerField()),
                ('exercise', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BloodPressure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systolic', models.IntegerField()),
                ('diastolic', models.IntegerField()),
                ('pulse', models.IntegerField()),
                ('recorded_at', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
