from django.db import models
from utils import text_convertor as tc


class Category(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = tc.uniq_slugify_rplc_space_dot_at(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
