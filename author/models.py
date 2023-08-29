from django.db import models
from utils import text_convertor as tc


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='images/Author', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    join_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = tc.uniq_slugify_rplc_space_dot_at(self, f"{self.first_name}{self.last_name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def salam(self):
        return f"{self.email} / {self.phone}"
