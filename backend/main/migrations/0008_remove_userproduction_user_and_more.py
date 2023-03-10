# Generated by Django 4.0.2 on 2022-12-01 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_is_consuming_account_consuming_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userproduction',
            name='user',
        ),
        migrations.RemoveField(
            model_name='solarpanel',
            name='userProduction',
        ),
        migrations.RemoveField(
            model_name='tv',
            name='userConsumption',
        ),
        migrations.RemoveField(
            model_name='windturbine',
            name='userProduction',
        ),
        migrations.AddField(
            model_name='solarpanel',
            name='producer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solar_panel', to='main.account'),
        ),
        migrations.AddField(
            model_name='tv',
            name='consumer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TV', to='main.account'),
        ),
        migrations.AddField(
            model_name='windturbine',
            name='producer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wind_turbine', to='main.account'),
        ),
        migrations.DeleteModel(
            name='UserConsumption',
        ),
        migrations.DeleteModel(
            name='UserProduction',
        ),
    ]
