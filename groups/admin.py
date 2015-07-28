from django.contrib import admin
from .models import Group, GroupMember, GroupRank, GroupInvitation

class GroupRankInline(admin.TabularInline):
    model = GroupRank
    extra = 0

class GroupMemberInline(admin.TabularInline):
    model = GroupMember
    extra = 0

class GroupInvitationInline(admin.TabularInline):
    model = GroupInvitation
    extra = 0

class GroupAdmin(admin.ModelAdmin):
    inlines = [GroupRankInline, GroupMemberInline, GroupInvitationInline]

admin.site.register(Group, GroupAdmin)
admin.site.register(GroupMember)
admin.site.register(GroupRank)
admin.site.register(GroupInvitation)
