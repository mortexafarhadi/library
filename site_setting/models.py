from django.db import models


class HeaderLink(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
