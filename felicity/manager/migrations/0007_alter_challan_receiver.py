# Generated by Django 5.0.6 on 2024-06-09 21:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_rename_reciever_challan_receiver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challan',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challanReceiver', to='manager.buyer'),
        ),
    ]