# Generated by Django 4.1.3 on 2022-11-13 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0005_alter_balance_transaction"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="transaction",
            options={"ordering": ["-time_create"]},
        ),
    ]
