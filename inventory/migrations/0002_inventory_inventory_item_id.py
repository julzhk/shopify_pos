# Generated by Django 3.0.4 on 2020-03-20 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='inventory_item_id',
            field=models.TextField(blank=True, max_length=32),
        ),
    ]
