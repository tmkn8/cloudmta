from django.contrib import admin
from .models import User, Member, QuizQuestion

admin.site.register(User)
admin.site.register(Member)
admin.site.register(QuizQuestion)
