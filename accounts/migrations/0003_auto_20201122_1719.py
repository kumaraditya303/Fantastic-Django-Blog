# -*- coding: utf-8 -*-
# Generated by Django 3.1.3 on 2020-11-22 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_auto_20201122_1657"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="picture",
            field=models.ImageField(
                blank=True,
                default="testing.jpeg",
                upload_to="thumbnail",
                verbose_name="Picture",
            ),
        ),
    ]
