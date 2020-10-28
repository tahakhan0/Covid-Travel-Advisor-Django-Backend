# Generated by Django 3.1.2 on 2020-10-24 13:25

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'APIs',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
                ('country_code', models.TextField(max_length=4)),
            ],
            options={
                'verbose_name_plural': 'Country',
            },
        ),
        migrations.CreateModel(
            name='MessagesFromAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('deaths', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('recovered', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('content', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=None)),
                ('test_required', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], default='No', max_length=3)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('api', models.ManyToManyField(blank=True, to='Messages.APIs')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages_country_code', to='Messages.country')),
                ('restricted_countries', models.ManyToManyField(blank=True, related_name='restricted_countries', to='Messages.Country')),
            ],
            options={
                'verbose_name_plural': 'Messages',
            },
        ),
    ]
