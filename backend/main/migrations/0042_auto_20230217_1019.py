# Generated by Django 3.0 on 2023-02-17 10:19

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_account_private_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('name', models.CharField(default='', max_length=40, verbose_name='Name')),
                ('is_prosumer', models.BooleanField(default=False)),
                ('consuming', models.IntegerField(default=0)),
                ('last_consumption', models.DateTimeField(default=django.utils.timezone.now)),
                ('producing', models.IntegerField(default=0)),
                ('last_production', models.DateTimeField(default=django.utils.timezone.now)),
                ('surplus', models.IntegerField(default=0)),
                ('address', models.CharField(default='', max_length=42)),
                ('private_key', models.CharField(default='', max_length=42)),
                ('todays_energy_mix', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None)),
                ('energy_mix_per_day', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None), blank=True, default=list, size=None)),
                ('overall_energy_mix', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None)),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='consumingobject',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='object',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='producingobject',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
