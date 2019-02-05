from django.db import models


class Order(models.Model):
    email = models.EmailField()
    telephone = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    price = models.FloatField()

    def __str__(self):
        return "Name: %s Email: %s" % (self.name, self.email)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'


class Category(models.Model):
    category = models.CharField(max_length=128)

    def __str__(self):
        return self.category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    price = models.FloatField()

