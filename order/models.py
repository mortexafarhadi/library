from __future__ import unicode_literals
from django.db import models

from account.models import User
from book.models import Book


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def calculate_total_price(self):
        total_amount = 0
        if self.is_paid:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.final_price * order_detail.count
        else:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.product.price * order_detail.count
        return total_amount


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    final_price = models.IntegerField(null=True, blank=True)
    count = models.SmallIntegerField(default=1)

    def get_total_price(self):
        return self.count * self.book.price

    def __str__(self):
        return str(self.order)


class OrderPayment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    serial = models.TextField()
    payment_id = models.TextField()
    price = models.IntegerField()
    date = models.TextField(default='-')
    card_number = models.TextField(default="****")
    idpay_track_id = models.IntegerField(default=0000)
    bank_track_id = models.TextField(default=0000)
    status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk) + "  |  " + str(self.order.id) + "  |  " + str(self.serial) + "  |  " + str(self.status)
