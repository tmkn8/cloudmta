from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Vehicle

@login_required
def vehicles_show(request, pk):
    """Wyświetl stronę o pojeździe"""
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if not vehicle.check_permissions(request.user):
        raise PermissionDenied
    return render(request, 'vehicles/show.html', {'vehicle': vehicle})
