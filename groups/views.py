from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Group

def get_group_object(request, pk):
    """Zwróć obiekt grupy

    Funkcja zapobiega powtarzaniu kodu do pobierania obiektu grupy.
    Zwraca kod HTTP 404, jeżeli użytkownik nie ma praw do przeglądania grupy."""
    group = Group.objects.get(pk=pk)
    if not group.can_user_access_group(user=request.user):
        raise HttpResponseForbidden()
    return group

@login_required
def groups_show_index(request, pk):
    """Strona główna panelu grupy"""
    group = get_group_object(request, pk)
    user_permissions = group.get_user_permissions(user=request.user)
    return render(request, 'groups/show/index.html', {'group': group,
        'user_permissions': user_permissions})

@login_required
def groups_show_members(request, pk):
    """Podstrona wyświetla wszystkich członków grupy"""
    group = get_group_object(request, pk)
    members = group.groupmembers.all()
    return render(request, 'groups/show/members.html', {'group': group,
        'members': members})

@login_required
def groups_show_ranks(request, pk):
    """Wyświetl stronę z rangami grupy"""
    group = get_group_object(request, pk)
    ranks = group.groupranks.all()
    return render(request, 'groups/show/ranks.html', {'group': group,
        'ranks': ranks})
