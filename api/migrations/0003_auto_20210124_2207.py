# Generated by Django 3.1.5 on 2021-01-24 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210124_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankdetail',
            name='bank_name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='bankdetail',
            name='district',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='bankdetail',
            name='state',
            field=models.CharField(max_length=31),
        ),
    ]
