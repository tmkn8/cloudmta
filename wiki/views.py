from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils.translation import ugettext as _
from django.core.exceptions import PermissionDenied
from .models import Article, Category

def index(request):
    categories = Category.objects.all()
    return render(request, 'wiki/index.html', {'categories': categories})

def article(request, cat, article):
    article = get_object_or_404(Article, slug=article)
    if article.visible_only_for_staff and not request.user.is_staff:
        raise PermissionDenied
    if cat != article.category.slug:
        return redirect(article.get_absolute_url())
    categories = Category.objects.all()
    return render(request, 'wiki/article.html', {'article': article,
        'categories': categories})
