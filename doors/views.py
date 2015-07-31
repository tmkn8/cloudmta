from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Door

@login_required
def doors_show(request, pk):
    """Wyświetl infomacje o drzwiach - panel drzwi"""
    door = get_object_or_404(Door, pk=pk)
    if not door.check_permissions(request.user):
        raise PermissionDenied
    return render(request, 'doors/show.html', {'door': door})
