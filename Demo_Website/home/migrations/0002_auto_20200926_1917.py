# Generated by Django 3.1.1 on 2020-09-26 13:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 26, 19, 17, 10, 816101), verbose_name='date added'),
        ),
    ]
