# Generated by Django 4.0.2 on 2022-12-01 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_account_last_consumption_account_last_production_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_consuming',
            new_name='consuming',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='is_producing',
            new_name='producing',
        ),
    ]
