# Generated by Django 5.0.6 on 2024-06-05 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_alter_entry_challan_challanentry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challan',
            old_name='reciever',
            new_name='receiver',
        ),
    ]