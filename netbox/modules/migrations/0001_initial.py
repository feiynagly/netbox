# Generated by Django 2.1.7 on 2019-03-05 09:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('serial', models.CharField(max_length=30, unique=True)),
                ('rate', models.IntegerField(default=10000)),
                ('type', models.PositiveSmallIntegerField(default=1)),
                ('reach', models.PositiveSmallIntegerField(default=10)),
                ('status', models.PositiveSmallIntegerField(default=1)),
                ('usage', models.CharField(blank=True, max_length=266)),
                ('slug', models.SlugField(unique=True)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules',
                                                   to='modules.Manufacturer')),
            ],
            options={
                'ordering': ['rate'],
            },
        ),
    ]
