from django.db import models

from src.utils.models import BaseModel


# Create your models here.
class Author(BaseModel):
    name = models.CharField('名字', max_length=10)
    email = models.EmailField('信箱', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'


class Publisher(BaseModel):
    name = models.CharField('名稱', max_length=10, unique=True)
    address = models.CharField('地址', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '出版社'
        verbose_name_plural = '出版社'


class Classification(BaseModel):
    name = models.CharField('名稱', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分類'
        verbose_name_plural = '分類'


class Tag(BaseModel):
    name = models.CharField('名稱', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '標籤'
        verbose_name_plural = '標籤'


class Book(BaseModel):
    name = models.CharField('書名', max_length=50)
    introduction = models.TextField('簡介')
    price = models.PositiveIntegerField('價格')
    authors = models.ManyToManyField(Author, verbose_name='作者')
    publisher = models.ForeignKey(
        Publisher,
        models.PROTECT,
        verbose_name='出版社',
    )
    classification = models.ForeignKey(
        Classification,
        models.PROTECT,
        verbose_name='分類',
    )
    tags = models.ManyToManyField(Tag, verbose_name='標籤')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '書籍'
        verbose_name_plural = '書籍'
