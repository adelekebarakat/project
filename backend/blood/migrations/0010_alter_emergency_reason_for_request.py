# Generated by Django 5.0.6 on 2024-06-24 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0009_alter_emergency_reason_for_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergency',
            name='reason_for_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blood.reasonforrequest'),
        ),
    ]
