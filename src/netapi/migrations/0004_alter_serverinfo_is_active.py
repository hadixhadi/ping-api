# Generated by Django 4.2.7 on 2023-11-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netapi', '0003_serverinfo_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverinfo',
            name='is_active',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
