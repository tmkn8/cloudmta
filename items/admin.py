from django.contrib import admin
from .models import Item, Order, OrderCategory, OrderType, Deposite, Delivery

class OrderInline(admin.TabularInline):
    model = Order
    extra = 0

class OrderCategoryAdmin(admin.ModelAdmin):
    inlines = [OrderInline]

admin.site.register(Item)
admin.site.register(OrderCategory, OrderCategoryAdmin)
admin.site.register(Order)
admin.site.register(Deposite)
admin.site.register(Delivery)
admin.site.register(OrderType)
