# -*- coding: utf-8 -*-
# Generated by Django 3.1.3 on 2020-11-22 10:26

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="Title")),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Newsletter",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "timestamp",
                    models.DateTimeField(auto_now=True, verbose_name="Timestamp"),
                ),
            ],
            options={
                "verbose_name": "newsletter",
                "verbose_name_plural": "newsletters",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Title")),
                ("overview", models.TextField(default="", verbose_name="Overview")),
                (
                    "timestamp",
                    models.DateTimeField(auto_now=True, verbose_name="Timestamp"),
                ),
                ("content", tinymce.models.HTMLField(default="<p>Hello World</p>")),
                (
                    "featured",
                    models.BooleanField(default=False, verbose_name="Featured"),
                ),
                (
                    "thumbnail",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="posts_thumbnail",
                        verbose_name="Thumbnail",
                    ),
                ),
                ("slug", models.SlugField(blank=True, null=True, verbose_name="Slug")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.author",
                        verbose_name="Author",
                    ),
                ),
                (
                    "category",
                    models.ManyToManyField(
                        related_name="post", to="blog.Category", verbose_name="Category"
                    ),
                ),
            ],
            options={
                "verbose_name": "Post",
                "verbose_name_plural": "Posts",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(auto_now=True, verbose_name="Timestamp"),
                ),
                ("content", models.TextField(verbose_name="Content")),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment",
                        to="blog.post",
                        verbose_name="post",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.author",
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "comment",
                "verbose_name_plural": "comments",
            },
        ),
    ]
