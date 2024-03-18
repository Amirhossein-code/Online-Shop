from django.db import models
from common.utils import custom_slugify
from autoslug import AutoSlugField


class Category(models.Model):
    title = models.CharField(max_length=355)
    slug = AutoSlugField(
        populate_from="title",
        unique=True,
        blank=True,
        null=True,
        slugify=custom_slugify,
    )
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="store/category/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_category = Category.objects.get(pk=self.pk)
            if self.title != old_category.title:
                self.slug = custom_slugify(self.title)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"
