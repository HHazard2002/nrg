# Generated by Django 4.0.2 on 2023-02-12 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_consumingobject_overall_expense_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumingobject',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='producingobject',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
