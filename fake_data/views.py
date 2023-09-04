from django.shortcuts import render
from faker import Faker

from author.models import Author
from book.models import Book
from category.models import Category
from publisher.models import Publisher


def fake_author(request, count):
    if request.method == 'GET':
        fake = Faker()
        fake_fa = Faker(locale='fa_IR')
        if count is not None and count > 0:
            for _ in range(count):
                author = Author(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    email=fake.email(),
                    birthday=fake.date(),
                    bio=fake.text(),
                    phone=fake.random_number(digits=11),
                )
                author.save()

            context = {
                "model": "Author",
                "count": count,
            }
            return render(request, 'fake_data/fake-data.html', context)


def fake_publisher(request, count):
    if request.method == 'GET':
        fake = Faker()
        fake_fa = Faker(locale='fa_IR')
        if count is not None and count > 0:
            for _ in range(count):
                publisher = Publisher(
                    name=fake.name(),
                    email=fake.email(),
                    phone=fake.random_number(digits=11),
                    address=fake.address(),
                    year_created=fake.date(),
                    about=fake.text()
                )
                publisher.save()

            context = {
                "model": "Publisher",
                "count": count,
            }
            return render(request, 'fake_data/fake-data.html', context)


def fake_category(request, count):
    if request.method == 'GET':
        fake = Faker()
        fake_fa = Faker(locale='fa_IR')
        if count is not None and count > 0:
            for _ in range(count):
                category = Category(
                    title=fake.name(),
                    code=fake.random_number(digits=10),
                    description=fake.text()
                )
                category.save()

            context = {
                "model": "Category",
                "count": count,
            }
            return render(request, 'fake_data/fake-data.html', context)


def fake_book(request, count):
    if request.method == 'GET':
        fake = Faker()
        fake_fa = Faker(locale='fa_IR')
        if count is not None and count > 0:
            author_ids = Author.objects.filter(is_active=True).values_list('id', flat=True)
            publisher_ids = Publisher.objects.filter(is_active=True).values_list('id', flat=True)
            category_ids = Category.objects.filter(is_active=True).values_list('id', flat=True)
            for _ in range(count):
                a_id = fake.random_choices(elements=tuple(author_ids), length=1)[0]
                p_id = fake.random_choices(elements=tuple(publisher_ids), length=1)[0]
                c_id = fake.random_choices(elements=tuple(category_ids), length=1)[0]
                book = Book(
                    title=fake.name(),
                    author_id=a_id,
                    publisher_id=p_id,
                    category_id=c_id,
                    price=fake.random_number(digits=6),
                    summary=fake.text(),
                    discount=fake.pyint(min_value=0, max_value=99, step=1),
                    page_count=fake.pyint(min_value=50, max_value=2000, step=1),
                    created_at=fake.date(),
                )
                book.save()

            context = {
                "model": "Book",
                "count": count,
            }
            return render(request, 'fake_data/fake-data.html', context)
