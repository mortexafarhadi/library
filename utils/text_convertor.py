from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from faker import Faker
from slugify import UniqueSlugify


def uniq_slugify_rplc_space(instance, text):
    Klass = instance.__class__
    text = text.replace(' ', '-')
    unique_slug = UniqueSlugify()
    unique_slug.safe_chars = ['-', '@', '.']
    slug = unique_slug(text)
    exist_slug = Klass.objects.filter(slug=slug).first()
    if exist_slug is None:
        return slug
    else:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=get_random_string(4)
        )
        return uniq_slugify_rplc_space(instance, new_slug)


def uniq_slugify_rplc_space_dot_at(instance, text):
    Klass = instance.__class__
    text = text.replace(' ', '-')
    text = text.replace('.', '-')
    text = text.replace('@', '-')
    unique_slug = UniqueSlugify()
    unique_slug.safe_chars = ['-']
    slug = unique_slug(text)
    exist_slug = Klass.objects.filter(slug=slug).first()
    if exist_slug is None:
        return slug
    else:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=get_random_string(4)
        )
        return uniq_slugify_rplc_space_dot_at(instance, new_slug)


def uniq_slugify_username(text):
    text = text.replace(' ', '-')
    text = text.replace('.', '-')
    text = text.replace('@', '-')
    unique_slug = UniqueSlugify()
    unique_slug.safe_chars = ['-']
    slug = unique_slug(text)
    User = get_user_model()
    exist_slug = User.objects.filter(username__iexact=slug).first()
    if exist_slug is None:
        return slug
    else:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=get_random_string(4)
        )
        return uniq_slugify_username(new_slug)


def uniq_username_number(digits=10):
    fake = Faker()
    User = get_user_model()
    uniq = fake.random_number(digits=digits, fix_len=True)
    usr = User.objects.filter(username__iexact=uniq).first()
    if usr is None:
        return uniq
    else:
        return uniq_username_number(digits)


def uniq_number_code(instance, digits=10):
    Klass = instance.__class__
    fake = Faker()
    uniq = fake.random_number(digits=digits, fix_len=True)
    usr = Klass.objects.filter(code__iexact=uniq).first()
    if usr is None:
        return uniq
    else:
        return uniq_number_code(instance, digits)


def uniq_number_activation_code(digits=20):
    User = get_user_model()
    fake = Faker()
    uniq = fake.random_number(digits=digits, fix_len=True)
    usr = User.objects.filter(activation_code__iexact=uniq).first()
    if usr is None:
        return uniq
    else:
        return uniq_number_activation_code(digits)
