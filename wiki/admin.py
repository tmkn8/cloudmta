from django.contrib import admin
from .models import Article, Category

class ArticleInline(admin.TabularInline):
    model = Article
    extra = 0
    show_change_link = True

class CategoryAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]
    prepopulated_fields = {
        'slug': ('name',)
    }

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
