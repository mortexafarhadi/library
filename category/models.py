from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
