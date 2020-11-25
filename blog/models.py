# -*- coding: utf-8 -*-
from io import BytesIO

from django.core.files.storage import default_storage
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from PIL import Image
from tinymce.models import HTMLField

from accounts.models import Author


class Category(models.Model):

    title = models.CharField(_("Title"), max_length=50)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class Post(models.Model):

    title = models.CharField(_("Title"), max_length=100)
    overview = models.TextField(_("Overview"), default="")
    timestamp = models.DateTimeField(_("Timestamp"), auto_now=True)

    content = HTMLField(default="<p>Hello World</p>")
    featured = models.BooleanField(_("Featured"), default=False)
    category = models.ManyToManyField(
        Category, verbose_name=_("Category"), related_name="post"
    )
    author = models.ForeignKey(
        Author, verbose_name=_("Author"), on_delete=models.CASCADE
    )
    thumbnail = models.ImageField(
        _("Thumbnail"), upload_to="thumbnail", default="testing.jpeg", blank=True
    )
    slug = models.SlugField(_("Slug"), blank=True, null=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Absolute URL for Post"""
        return reverse("post_detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        """Update URL for Post"""
        return reverse("post_update", kwargs={"slug": self.slug})

    def get_delete_url(self):
        """Delete URL for Post"""
        return reverse("post_delete", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        if self.thumbnail:
            img = Image.open(default_storage.open(self.thumbnail.name))
            if img.height > 1080 or img.width > 1920:  # pragma:no cover
                output_size = (1920, 1080)
                img.thumbnail(output_size)
                buffer = BytesIO()
                img.save(buffer, format="JPEG")
                default_storage.save(self.thumbnail.name, buffer)


class Comment(models.Model):

    user = models.ForeignKey(Author, verbose_name=_("user"), on_delete=models.CASCADE)
    timestamp = models.DateTimeField(_("Timestamp"), auto_now=True)
    content = models.TextField(_("Content"))
    post = models.ForeignKey(
        Post, verbose_name=_("post"), on_delete=models.CASCADE, related_name="comment"
    )

    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")

    def __str__(self):
        return self.user.user.username


class Newsletter(models.Model):

    email = models.EmailField(_("Email"), max_length=254)
    timestamp = models.DateTimeField(_("Timestamp"), auto_now=True)

    class Meta:
        verbose_name = _("newsletter")
        verbose_name_plural = _("newsletters")

    def __str__(self):
        return self.email
