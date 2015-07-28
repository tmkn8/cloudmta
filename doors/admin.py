from django.contrib import admin
from django.utils.translation import ugettext as _
from .models import DoorPickup, Door, Shop, Clothes, InteriorDetail, Object

class DoorPickupInline(admin.TabularInline):
    show_change_link = True
    model = DoorPickup
    extra = 0
    fields = ('name', 'locked', 'parentid')

class ShopInline(admin.TabularInline):
    show_change_link = True
    model = Shop
    extra = 0

class ClothesInline(admin.TabularInline):
    show_change_link = True
    model = Clothes
    extra = 0

class DoorAdmin(admin.ModelAdmin):
    inlines = [DoorPickupInline, ShopInline, ClothesInline]

class DoorPickupAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('parentid', 'name', 'locked')
        }),
        (_('Wejście'), {
            'fields': ('inx', 'iny', 'inz', 'indim', 'inint', 'inmodel',
                'inangle')
        }),
        (_('Wyjście'), {
            'fields': ('outx', 'outy', 'outz', 'outdim', 'outint', 'outmodel',
                'outangle')
        }),
    )

admin.site.register(Door, DoorAdmin)
admin.site.register(DoorPickup, DoorPickupAdmin)
admin.site.register(Shop)
admin.site.register(Clothes)
admin.site.register(InteriorDetail)
admin.site.register(Object)
