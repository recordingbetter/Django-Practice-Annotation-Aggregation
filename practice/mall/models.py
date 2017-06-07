
from django.db import models


class Product(models.Model):
    name = models.CharField('이름', max_length = 150, unique = True)
    price = models.IntegerField('가격')

    def __str__(self):
        return '{} : {}'.format(self.name, self.price)


class OrderLog(models.Model):
    product = models.ForeignKey(Product)
    created = models.DateTimeField()

    def __str__(self):
        return '{} : {}'.format(self.product.name, self.created)
