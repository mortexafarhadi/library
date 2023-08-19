from django.db import models

from author.models import Author
from category.models import Category
from publisher.models import Publisher


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    summary = models.TextField(blank=True, null=True)
    page_count = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/Book', blank=True, null=True)

    def __str__(self):
        return self.title