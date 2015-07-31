from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils.translation import ugettext as _
from django.core.exceptions import PermissionDenied
from .models import Article, Category

def index(request):
    """Strona główna Wiki

    Wyświetla wszystkie kategorie i artykuły"""
    categories = Category.objects.all()
    return render(request, 'wiki/index.html', {'categories': categories})

def article(request, cat, article):
    """Wyświetl pojedynczy artykuł na Wiki"""
    article = get_object_or_404(Article, slug=article)
    # Jeżeli artykuł ma być widoczny tylko dla administracji, to wypluj 403
    if article.visible_only_for_staff and not request.user.is_staff:
        raise PermissionDenied
    # Jeżeli kategoria się nie zgadza w URL, to przekieruj na poprawne URL
    if cat != article.category.slug:
        return redirect(article.get_absolute_url())
    categories = Category.objects.all()
    return render(request, 'wiki/article.html', {'article': article,
        'categories': categories})
