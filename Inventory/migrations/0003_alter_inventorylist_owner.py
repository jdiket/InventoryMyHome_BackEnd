# Generated by Django 3.2.5 on 2021-07-09 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Inventory', '0002_alter_inventorylist_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorylist',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inventorylist', to=settings.AUTH_USER_MODEL),
        ),
    ]
