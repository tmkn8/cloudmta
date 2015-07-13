from django.contrib import admin
from .models import User, Member, QuizQuestion

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('email', 'username', 'password', 'last_login')

class MemberAdmin(admin.ModelAdmin):
    readonly_fields = ('uid', 'username', 'email')
    exclude = ('password', 'salt')

admin.site.register(User, UserAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(QuizQuestion)
