# Generated by Django 3.0.6 on 2020-06-19 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200619_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressbook',
            name='favorite',
            field=models.BooleanField(),
        ),
    ]
