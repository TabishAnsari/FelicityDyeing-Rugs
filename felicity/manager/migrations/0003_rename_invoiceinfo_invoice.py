# Generated by Django 5.0.6 on 2024-06-01 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_remove_buyer_code_remove_selfinfo_code'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Invoiceinfo',
            new_name='Invoice',
        ),
    ]
