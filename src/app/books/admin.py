from django.contrib import admin

from .models import Author, Publisher, Classification, Tag, Book

# Register your models here.
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Classification)
admin.site.register(Tag)
admin.site.register(Book)
