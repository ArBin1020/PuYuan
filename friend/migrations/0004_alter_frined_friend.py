# Generated by Django 4.2.5 on 2023-10-14 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friend', '0003_alter_frined_read_alter_frined_relation_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frined',
            name='friend',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friend', to=settings.AUTH_USER_MODEL),
        ),
    ]
