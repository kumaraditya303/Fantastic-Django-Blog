from io import BytesIO

from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
from PIL import Image
from tinymce.models import HTMLField


class Category(models.Model):
    """
    Category Model
    """
    title = models.CharField(_("Title"), max_length=50)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})


class Author(models.Model):
    """
    Author Model
    """
    user = models.OneToOneField(
        User, verbose_name=_("User"), on_delete=models.CASCADE)
    picture = models.ImageField(
        _("Picture"), upload_to='profile')

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.user.get_full_name()

    def get_absolute_url(self):
        return reverse("Author_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(default_storage.open(self.picture.name))
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            buffer = BytesIO()
            img.save(buffer, format='JPEG')
            default_storage.save(self.picture.name, buffer)


class Post(models.Model):
    """
    Post Model
    """
    title = models.CharField(_("Title"), max_length=100)
    overview = models.TextField(_("Overview"), default='')
    timestamp = models.DateTimeField(
        _("Timestamp"), auto_now=True)

    content = HTMLField()
    featured = models.BooleanField(_("Featured"), default=False)
    category = models.ManyToManyField(
        Category, verbose_name=_("Category"), related_name='post')
    author = models.ForeignKey(Author, verbose_name=_(
        "Author"), on_delete=models.CASCADE)
    thumbnail = models.ImageField(
        _("Thumbnail"), upload_to='posts_thumbnail', default='thumbnail.jpg')

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(default_storage.open(self.thumbnail.name))
        if img.height > 1080 or img.width > 1920:
            output_size = (1920, 1080)
            img.thumbnail(output_size)
            buffer = BytesIO()
            img.save(buffer, format='JPEG')
            default_storage.save(self.thumbnail.name, buffer)


class Comment(models.Model):
    """
    Comment Model
    """
    user = models.ForeignKey(Author, verbose_name=_(
        "user"), on_delete=models.CASCADE)
    timestamp = models.DateTimeField(
        _("Timestamp"), auto_now=True)
    content = models.TextField(_("Content"))
    post = models.ForeignKey(Post, verbose_name=_(
        "post"), on_delete=models.CASCADE, related_name='comment')

    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")

    def __str__(self):
        return self.user.user.username

    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={"pk": self.pk})


class Newsletter(models.Model):
    """
    Newsletter Model
    """
    email = models.EmailField(_("Email"), max_length=254)
    timestamp = models.DateTimeField(_("Timestamp"), auto_now=True)

    class Meta:
        verbose_name = _("newsletter")
        verbose_name_plural = _("newsletters")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("newsletter_detail", kwargs={"pk": self.pk})
