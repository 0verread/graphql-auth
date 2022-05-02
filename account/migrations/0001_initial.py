# Generated by Django 3.0 on 2022-04-22 12:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('full_name', models.CharField(blank=True, max_length=256)),
                ('username', models.CharField(max_length=256, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.TextField()),
                ('date_jointed', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]