from django.contrib import admin
from django.apps import apps
from .models import User, MyBBMember, QuizQuestion, FriendRequest

class CharacterInline(admin.TabularInline):
    model = apps.get_model('characters', 'Character')
    fields = ('name', 'facecode', 'hp', 'money', 'sex', 'ajtime', 'bwtime',
        'dob')
    can_delete = False
    show_change_link = True
    extra = 0

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('email', 'username', 'password', 'last_login')
    inlines = [CharacterInline]

class MyBBMemberAdmin(admin.ModelAdmin):
    readonly_fields = ('uid', 'username', 'email')
    exclude = ('password', 'salt')

admin.site.register(User, UserAdmin)
admin.site.register(MyBBMember, MyBBMemberAdmin)
admin.site.register(QuizQuestion)
admin.site.register(FriendRequest)
