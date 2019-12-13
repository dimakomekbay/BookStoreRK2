from django.conf.urls import url
from django.views.generic import TemplateView
from ecomapp.views import (
    base_view,
    category_view,
    product_view,
    cart_view,
    add_to_cart_view,
    remove_from_cart_view,
    change_item_quantity,
    checkout_view,
    order_create_view,
    make_order_view,
    account_view,
    registration_view,
    login_view
    )

urlpatterns = [
    url(r'^category/(?P<category_slug>[-\w]+)/$', category_view, name='category_detail'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', product_view, name='product_detail'),
    url(r'^add_to_cart/$', add_to_cart_view, name='add_to_cart'),
    url(r'^remove_from_cart/$', remove_from_cart_view, name='remove_from_cart'),
    url(r'^change_item_quantity/$', change_item_quantity, name='change_item_quantity'),
    url(r'^cart/$', cart_view, name='cart'),
    url(r'^checkout/$', checkout_view, name='checkout'),
    url(r'^order/$', order_create_view, name='create_order'),
    url(r'^make_order/$', make_order_view, name='make_order'),
    url(r'^Thank_you/$', TemplateView.as_view(template_name='Thank_you.html'), name='Thank_you'),
    url(r'^account/$', account_view, name='account'),
    url(r'^registration/$', registration_view, name='registration'),
    url(r'^login/$', login_view, name='login'),
    url(r'^$', base_view, name='base'),

]
