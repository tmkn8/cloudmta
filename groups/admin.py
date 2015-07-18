from django.contrib import admin
from .models import Group, GroupMember, GroupRank, GroupInvitation

admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(GroupRank)
admin.site.register(GroupInvitation)
