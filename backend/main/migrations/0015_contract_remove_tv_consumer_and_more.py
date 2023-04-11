# Generated by Django 4.0.2 on 2022-12-13 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_rename_consumer_producingobject_producer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('address', models.CharField(default='', max_length=42)),
            ],
        ),
        migrations.RemoveField(
            model_name='tv',
            name='consumer',
        ),
        migrations.RemoveField(
            model_name='windturbine',
            name='producer',
        ),
        migrations.DeleteModel(
            name='SolarPanel',
        ),
        migrations.DeleteModel(
            name='TV',
        ),
        migrations.DeleteModel(
            name='WindTurbine',
        ),
    ]
