from django import template
from jalali_date import date2jalali, datetime2jalali

register = template.Library()


@register.filter(name='to_jalali_date')
def to_jalali_date(value):
    return date2jalali(value)


@register.filter(name='to_jalali_datetime')
def to_jalali_datetime(value):
    datetime = datetime2jalali(value)
    x = str(datetime).index(".")
    datetime = str(datetime)[:x]
    return datetime


@register.filter(name='to_jalali_time')
def to_jalali_time(value):
    datetime = datetime2jalali(value)
    x = str(datetime).index(" ")
    datetime = str(datetime)[x:]
    return datetime


# @register.filter(name='three_digit_currency')
# def three_digit_currency(value: str):
#     text_str = str(value)
#     parts = [text_str[i:i + 4] for i in range(0, len(text_str), 4)]
#     res = '-'.join(parts)
#     return res + "تومان "


@register.filter(name='three_digit_currency')
def three_digit_currency(value: int):
    return '{:,}'.format(value) + " تومان"
