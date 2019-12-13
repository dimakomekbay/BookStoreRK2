# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})



class Type(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)


class ProductManager(models.Manager):

    def all(self, *args, **kwargs):
        return super(ProductManager, self).get_queryset().filter(available=True)

class Product(models.Model):

    category = models.ForeignKey(Category, default=None)
    # type = models.ForeignKey(Type, None)
    title = models.CharField(max_length = 200)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=9, decimal_places=0)
    available = models.BooleanField(default=True)
    objects = ProductManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})


# class Book(models.Model):
#
#     BOOK_CHOICES = (
#         ('Fantasy', 'Thriller', 'Roman'),
#         ('Drama', 'Art'),
#     )
#     title = models.CharField(max_length = 100, choices = BOOK_CHOICES)

class CartItem(models.Model):

    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places=0, default=0)



    def __unicode__(self):
        return "Cart item for product {0}".format(self.product.title)

class Cart(models.Model):

    items = models.ManyToManyField(CartItem, blank=True)
    cart_total = models.DecimalField(max_digits=9, decimal_places=0, default=0)

    def __unicode__(self):
        return str(self.id)

    def add_to_cart(self, product_slug):
        cart = self
        product = Product.objects.get(slug = product_slug)
        new_item, _ = CartItem.objects.get_or_create(product=product, item_total=product.price)
        if new_item not in cart.items.all():
            cart.items.add(new_item)
            cart.save()

    def remove_from_cart(self, product_slug):
        cart = self
        product = Product.objects.get(slug = product_slug)
        for cart_item in cart.items.all():
            if cart_item.product == product:
                cart.items.remove(cart_item)
                cart.save()


ORDER_STATUS_CHOICES = (
        ('Received for processing', 'Received for processing'),
        ('Processing', 'Processing'),
        ('Payed', 'Payed')
)

class Order(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    items = models.ManyToManyField(Cart)
    total = models.DecimalField(max_digits=9, decimal_places=0, default=0)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    buying_type = models.CharField(max_length=40, choices=(('Self', 'Self'), ('Delivery', 'Delivery')), default='Self')
    date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()
    status = models.CharField(max_length=100, choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_CHOICES[0][0])


    def __unicode__(self):
        return "Order №{0}".format(str(self.id))
