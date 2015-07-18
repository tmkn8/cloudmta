from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.utils.translation import ugettext as _
from .models import Group
from .forms import RankEditForm, MemberEditForm

def get_group_object(request, pk):
    """Zwróć obiekt grupy

    Funkcja zapobiega powtarzaniu kodu do pobierania obiektu grupy.
    Zwraca kod HTTP 404, jeżeli użytkownik nie ma praw do przeglądania grupy."""
    group = get_object_or_404(Group, pk=pk)
    if not group.can_user_access_group(user=request.user):
        raise PermissionDenied
    return group

def allow_only_leaders(group, user):
    """Ogranicz dostęp tylko dla liderów

    Użyj tej funkcji w miejscach, gdzie chcesz aby dostęp
    mieli tylko liderzy grupy."""
    if not group.can_user_manage_group(user=user):
        raise PermissionDenied

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
    ranks = group.groupranks.all()
    return render(request, 'groups/show/members.html', {'group': group,
        'ranks': ranks})

@login_required
def groups_show_members_edit(request, pk, member_id):
    """Podstrona wyświetla edycję członka grupy"""
    group = get_group_object(request, pk)
    member = get_object_or_404(group.groupmembers, pk=member_id)
    allow_only_leaders(group=group, user=request.user)
    if request.method == 'POST':
        form = MemberEditForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, _("Ranga członka %s została zmieniona."
                % member.userid))
            return redirect('groups:show:members', group.pk)
    else:
        form = MemberEditForm(instance=member)

    return render(request, 'groups/show/members_edit.html', {'group': group,
        'member': member, 'form': form})

@login_required
def groups_show_members_delete(request, pk, member_id):
    """Postrona do kasowania członka z panelu"""
    group = get_group_object(request, pk)
    member = get_object_or_404(group.groupmembers, pk=member_id)
    allow_only_leaders(group=group, user=request.user)
    if request.method == 'POST':
        member.delete()
        messages.success(request, _("%s został(a) usunięty(a) z panelu."
            % member.userid))
        return redirect('groups:show:members', group.pk)
    else:
        return render(request, 'groups/show/members_delete.html',
            {'group': group, 'member': member})

@login_required
def groups_show_ranks(request, pk):
    """Wyświetl stronę z rangami grupy"""
    group = get_group_object(request, pk)
    ranks = group.groupranks.all()
    return render(request, 'groups/show/ranks.html', {'group': group,
        'ranks': ranks})

@login_required
def groups_show_ranks_edit(request, pk, rank_id):
    """Wyświetl formularz edycji rangi"""
    group = get_group_object(request, pk)
    rank = get_object_or_404(group.groupranks, pk=rank_id)
    allow_only_leaders(group=group, user=request.user)

    if request.method == 'POST':
        # Stwórz nową tabelę do odebrania tego zapytania POST, ponieważ Django
        # nie pozwala na modyfikację request.POST bezpośrednio, a musimy to zrobić
        # żeby podmienić perms.
        modified_post = {}
        for key in request.POST:
            modified_post[key] = request.POST[key]
        # Pobierz uprawnienia w formacie zgodnym z JSONField
        modified_post['perms'] = rank.convert_form_permissions_to_perms_field(request.POST)
        form = RankEditForm(modified_post, instance=rank)
        if form.is_valid():
            form.save()
            messages.success(request, _("Ranga %s została zapisana." % rank))
            return redirect('groups:show:ranks', group.pk)
    else:
        form = RankEditForm(instance=rank)
    return render(request, 'groups/show/ranks_edit.html', {'group': group,
        'rank': rank, 'form': form})

@login_required
def groups_show_ranks_delete(request, pk, rank_id):
    """Wyświetl formularz kasowania rangi"""
    group = get_group_object(request, pk)
    rank = get_object_or_404(group.groupranks, pk=rank_id)
    allow_only_leaders(group=group, user=request.user)
    if request.method == 'POST':
        if rank.defaultrank:
            messages.error(request, _('Nie możesz skasować domyślnej rangi.'))
            return redirect('groups:show:ranks', group.pk)

        if rank.groupmembers.all().count():
            messages.error(request, _('Nie możesz skasować rangi, do której '
            'przypisani są członkowie.'))
            return redirect('groups:show:ranks', group.pk)

        rank.delete()
        messages.success(request, _("Ranga %s została skasowana." % rank))
        return redirect('groups:show:ranks', group.pk)
    else:
        return render(request, 'groups/show/ranks_delete.html', {'group': group,
            'rank': rank})
