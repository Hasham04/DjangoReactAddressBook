# Generated by Django 3.0.6 on 2020-06-20 23:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200619_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressbook',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
    ]
