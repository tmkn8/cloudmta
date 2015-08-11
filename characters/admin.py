from django.contrib import admin
from .models import Character, StartSkin, Facecode, LoginLog, PenaltyLog
from items.models import Item
from vehicles.models import Vehicle
from groups.models import GroupMember

class GroupMemberInline(admin.TabularInline):
    model = GroupMember
    extra = 0

class FacecodeInline(admin.TabularInline):
    model = Facecode
    extra = 0

class PenaltyLogInline(admin.TabularInline):
    model = PenaltyLog
    extra = 0

class CharacterAdmin(admin.ModelAdmin):
    inlines = [GroupMemberInline, FacecodeInline, PenaltyLogInline]

admin.site.register(Character, CharacterAdmin)
admin.site.register(StartSkin)
admin.site.register(Facecode)
admin.site.register(LoginLog)
admin.site.register(PenaltyLog)
