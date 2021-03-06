# Generated by Django 3.2.5 on 2021-08-28 16:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('availability', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(upload_to='photos/menu_items/main')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/menu_items/other')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/menu_items/other')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/menu_items/other')),
                ('date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='restaurants.restaurant')),
            ],
        ),
    ]
