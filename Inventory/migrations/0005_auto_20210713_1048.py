# Generated by Django 3.2.5 on 2021-07-13 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0004_auto_20210713_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='serial',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='where_purchased',
            field=models.CharField(default='Unknown', max_length=200),
        ),
    ]