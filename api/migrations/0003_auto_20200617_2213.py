# Generated by Django 3.0.6 on 2020-06-17 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200617_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressbook',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='addressbook',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
