# Generated by Django 4.2.5 on 2023-10-05 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipManager', '0004_alter_ipaddress_status'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='ipaddress',
            table='ipManager_ipaddress',
        ),
    ]