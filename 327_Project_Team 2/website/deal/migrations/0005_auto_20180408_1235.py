# Generated by Django 2.0.3 on 2018-04-08 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0004_deal_user_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='deal_logo',
        ),
        migrations.AddField(
            model_name='deal',
            name='thumbnail',
            field=models.FileField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
