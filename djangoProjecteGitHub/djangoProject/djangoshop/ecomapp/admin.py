# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ecomapp.models import Category, Type, Product, CartItem, Cart, Order

# Register your models here.
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order)
