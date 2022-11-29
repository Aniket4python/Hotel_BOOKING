# Generated by Django 4.1.1 on 2022-11-14 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_alter_amenities_uid_alter_hotel_uid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelbooking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_booking', to=settings.AUTH_USER_MODEL),
        ),
    ]
