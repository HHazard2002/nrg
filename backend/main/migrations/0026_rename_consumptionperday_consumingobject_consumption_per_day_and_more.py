# Generated by Django 4.0.2 on 2023-02-13 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_rename_active_consumingobject_is_active_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consumingobject',
            old_name='consumptionPerDay',
            new_name='consumption_per_day',
        ),
        migrations.RenameField(
            model_name='consumingobject',
            old_name='todaysConsumption',
            new_name='todays_consumption',
        ),
        migrations.RenameField(
            model_name='producingobject',
            old_name='consumptionPerDay',
            new_name='consumption_per_day',
        ),
        migrations.RenameField(
            model_name='producingobject',
            old_name='todaysConsumption',
            new_name='todays_consumption',
        ),
    ]