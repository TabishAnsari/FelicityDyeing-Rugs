# Generated by Django 5.0.6 on 2024-05-30 04:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=32)),
                ('gstin', models.CharField(max_length=32)),
                ('code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SelfInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=32)),
                ('gstin', models.CharField(max_length=32)),
                ('code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Challan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challanReciever', to='manager.buyer')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challanSender', to='manager.selfinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Invoiceinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoiceBuyer', to='manager.buyer')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoiceSeller', to='manager.selfinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('particulars', models.CharField(max_length=64)),
                ('hsn', models.IntegerField()),
                ('shade', models.CharField(max_length=64)),
                ('prgnum', models.IntegerField()),
                ('dyeType', models.CharField(max_length=64)),
                ('qty', models.FloatField()),
                ('rate', models.FloatField()),
                ('amount', models.FloatField()),
                ('challan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challanEntry', to='manager.challan')),
                ('invoicenum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoiceEntry', to='manager.invoiceinfo')),
            ],
        ),
    ]
