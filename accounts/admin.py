from django.contrib import admin
from .models import User, MyBBMember, QuizQuestion
from characters.models import Character

class CharacterInline(admin.TabularInline):
    model = Character
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
