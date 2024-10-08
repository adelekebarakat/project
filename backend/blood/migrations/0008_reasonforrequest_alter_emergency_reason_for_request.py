# Generated by Django 5.0.6 on 2024-06-24 08:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0007_rename_address_emergency_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReasonForRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=225)),
            ],
        ),
        migrations.AlterField(
            model_name='emergency',
            name='reason_for_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blood.reasonforrequest'),
        ),
    ]
