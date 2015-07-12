from django.contrib import admin
from .models import Item, Order, OrderCategory, OrderType, Deposite, Delivery

admin.site.register(Item)
admin.site.register(OrderCategory)
admin.site.register(Order)
admin.site.register(Deposite)
admin.site.register(Delivery)
admin.site.register(OrderType)
