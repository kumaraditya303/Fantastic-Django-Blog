# -*- coding: utf-8 -*-
from io import BytesIO

from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
from PIL import Image


class Author(models.Model):
    """
    Author Model
    """

    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    picture = models.ImageField(
        _("Picture"), upload_to="profile", blank=True, null=True
    )

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.user.get_full_name()

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.picture:
            img = Image.open(default_storage.open(self.picture.name))
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                buffer = BytesIO()
                img.save(buffer, format="JPEG")
                default_storage.save(self.picture.name, buffer)
