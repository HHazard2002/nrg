# Generated by Django 4.0.2 on 2023-02-08 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_account_surplus'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumingobject',
            name='overall_consumption',
            field=models.IntegerField(default=0),
        ),
    ]
