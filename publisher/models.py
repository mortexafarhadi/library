from django.db import models
from utils import text_convertor as tc


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    year_created = models.DateField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to='images/Publisher', null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = tc.uniq_slugify_rplc_space_dot_at(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
