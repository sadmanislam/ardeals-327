# Generated by Django 2.0.3 on 2018-04-08 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0007_auto_20180408_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deal',
            old_name='street',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='deal',
            name='city',
            field=models.CharField(default='Dhaka', max_length=550),
        ),
    ]
