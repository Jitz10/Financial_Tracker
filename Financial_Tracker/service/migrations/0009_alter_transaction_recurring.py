# Generated by Django 5.0.1 on 2024-02-19 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_alter_transaction_amount_alter_transaction_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='recurring',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
