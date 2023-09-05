import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from decouple import config
from idpay.api import IDPayAPI

import uuid

from order.models import Order, OrderDetail, OrderPayment
from book.models import Book

Payment_CallbackUrl = 'order/payment/return'


def add_product_to_order(request: HttpRequest):
    book_id = int(request.GET.get('book_id'))
    count = int(request.GET.get('count'))
    if count <= 0:
        result = {
            'status': 'invalid_count',
            'message': "تعداد وارد شده صحیح نیست",
            'confirm_button_text': 'باشه ممنون',
            'icon': "error"
        }
    else:
        if request.user.is_authenticated:
            user = request.user
            book = Book.objects.filter(id=book_id, is_active=True, is_delete=False).first()
            if book is not None:
                current_order, created = Order.objects.get_or_create(user=user, is_paid=False)
                current_order_detail: OrderDetail = current_order.orderdetail_set.filter(book=book).first()
                if current_order_detail is not None:
                    current_order_detail.count += count
                    current_order_detail.save()
                else:
                    new_order_detail = OrderDetail(order=current_order, book=book, count=count)
                    new_order_detail.save()

                result = {
                    'status': 'success',
                    'message': "محصول مورد نظر به سبد خرید اضافه شد",
                    'confirm_button_text': 'باشه ممنون',
                    'icon': "success"
                }
            else:
                result = {
                    'status': 'product_not_found',
                    'message': "محصول مورد نظر یافت نشد",
                    'confirm_button_text': 'باشه ممنون',
                    'icon': "error"
                }
        else:
            result = {
                'status': 'user_not_auth',
                'message': "کاربر احراز هویت نشده است لطفا وارد شوید",
                'confirm_button_text': 'باشه ممنون',
                'icon': "error"
            }
    return JsonResponse(result)


def payment_init():
    base_url = config('BASE_URL', default='http://127.0.0.1', cast=str)
    api_key = config('IDPAY_API_KEY', default='', cast=str)
    sandbox = config('IDPAY_SANDBOX', default=True, cast=bool)

    return IDPayAPI(api_key, base_url, sandbox)


@login_required
def payment_start(request):
    if request.method == 'POST':
        current_order, created = Order.objects.get_or_create(user=request.user, is_paid=False)
        total_price = current_order.calculate_total_price() * 10  # for Toman
        serial = uuid.uuid1()

        payer = {
            'name': current_order.user.__str__(),
            'phone': current_order.user.phone,
            'mail': current_order.user.email,
            'desc': "Payment for order : " + str(current_order.id),
        }

        record = OrderPayment(order_id=current_order.id, serial=serial, price=int(total_price))
        record.save()

        idpay_payment = payment_init()
        result = idpay_payment.payment(str(serial), total_price, Payment_CallbackUrl, payer)

        if 'id' in result:
            record.status = 1
            record.payment_id = result['id']
            record.save()
            print(result['link'])
            return redirect(result['link'])

        else:
            txt = result['message']
    else:
        txt = "Bad Request"

    return render(request, 'order/error.html', {'txt': txt})


@csrf_exempt
def payment_return(request):
    if request.method == 'POST':
        pid = request.POST.get('id')
        status = request.POST.get('status')
        pidtrack = request.POST.get('track_id')
        serial = request.POST.get('order_id')
        amount = request.POST.get('amount')
        card = request.POST.get('card_no')
        date = request.POST.get('date')
        if OrderPayment.objects.filter(serial=serial, payment_id=pid, price=amount, status=1).count() == 1:

            idpay_payment = payment_init()

            payment = OrderPayment.objects.get(payment_id=pid, price=amount)
            payment.status = status
            payment.date = str(date)
            payment.card_number = card
            payment.idpay_track_id = pidtrack
            payment.save()

            if str(status) == '10':
                result = idpay_payment.verify(pid, payment.order_id)

                current_order = Order.objects.get(id=payment.order.id, is_paid=False)
                order_details = current_order.orderdetail_set.all()
                for order_detail in order_details:
                    order_detail.final_price = order_detail.get_total_price()
                    order_detail.save()
                current_order.is_paid = True
                current_order.payment_date = datetime.datetime.now()
                current_order.save()

                if 'status' in result:
                    payment.status = result['status']
                    payment.bank_track_id = result['payment']['track_id']
                    payment.save()
                    current_order = Order.objects.get(id=payment.order.id, is_paid=False)
                    order_details = current_order.orderdetail_set.all()
                    for order_detail in order_details:
                        order_detail.final_price = order_detail.product.price
                        order_detail.save()
                    current_order.is_paid = True
                    current_order.payment_date = datetime.datetime.now()
                    current_order.save()

                    return render(request, 'order/error.html', {'txt': result['message']})

                else:
                    txt = result['message']

            else:
                txt = "Error Code : " + str(status) + "   |   " + "Description : " + idpay_payment.get_status(status)

        else:
            txt = "Order Not Found"

    else:
        txt = "Bad Request"

    return render(request, 'order/error.html', {'txt': txt})
