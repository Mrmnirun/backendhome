# Generated by Django 3.2.5 on 2021-09-22 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_items', '0002_menuitem_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
