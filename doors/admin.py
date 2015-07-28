from django.contrib import admin
from django.utils.translation import ugettext as _
from .models import DoorPickup, Door

class DoorPickupInline(admin.TabularInline):
    show_change_link = True
    model = DoorPickup
    extra = 0
    fields = ('name', 'locked', 'parentid')

class DoorAdmin(admin.ModelAdmin):
    inlines = [DoorPickupInline]

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
