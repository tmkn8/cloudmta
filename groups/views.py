from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.utils.translation import ugettext as _
from .models import Group, GroupRank
from .forms import RankEditForm, MemberEditForm, CreateGroupInvitationForm

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

@login_required
def groups_show_ranks_default_rank(request, pk):
    """Wyświetl formularz do zmiany domyślnej rangi"""
    group = get_group_object(request, pk)
    allow_only_leaders(group=group, user=request.user)
    ranks = group.groupranks.all()
    if request.method == 'POST':
        # Pobierz wybraną rangę i sprawdź czy istnieje.
        try:
            new_default_rank = ranks.get(pk=request.POST['default_rank'])
        except GroupRank.DoesNotExist:
            messages.error(request, _('Wybrana ranga nie istnieje.'))
            return redirect('groups:show:ranks_default_rank', group.pk)

        # Wyzeruj wszystkie domyślne rangi.
        ranks.update(defaultrank=False)
        # Ustaw wybraną rangę jako domyślną.
        new_default_rank.defaultrank = True
        new_default_rank.save()
        messages.success(request, _('Domyślna ranga została zmieniona.'))
        return redirect('groups:show:ranks', group.pk)
    return render(request, 'groups/show/ranks_default_rank.html', {'group': group,
        'ranks': ranks})

@login_required
def groups_show_invitations(request, pk):
    """Wyświetl listę aktywnych zaproszeń z grupy"""
    group = get_group_object(request, pk)
    invitations = group.groupinvitations.order_by('-pk').all()
    return render(request, 'groups/show/invitations.html', {'group': group,
        'invitations': invitations})

@login_required
def groups_show_invitations_create(request, pk):
    """Wyświetl formularz zapraszania graczy do grupy"""
    group = get_group_object(request, pk)
    allow_only_leaders(group=group, user=request.user)
    if request.method == 'POST':
        form = CreateGroupInvitationForm(request.POST)
        if form.is_valid():
            invitation = form.save(commit=False)

            if group.groupmembers.filter(userid=invitation.character):
                messages.error(request, _("Ta postać jest obecnie w grupie."))
                return redirect('groups:show:invitations_create', group.pk)

            if group.groupinvitations.filter(character=invitation.character).count():
                messages.error(request, _("Ta postać jest już zaproszona."))
                return redirect('groups:show:invitations_create', group.pk)

            invitation.invited_by = request.user
            invitation.group = group
            invitation.save()
            messages.success(request, _("Stworzyłeś zaproszenie dla %s" %
                invitation.character))
            return redirect('groups:show:invitations', group.pk)
    else:
        form = CreateGroupInvitationForm()
    return render(request, 'groups/show/invitations_create.html', {'group': group,
        'form': form})

@login_required
def groups_show_invitations_delete(request, pk, invitation_id):
    """Usuń zaproszenie do grupy."""
    group = get_group_object(request, pk)
    allow_only_leaders(group=group, user=request.user)
    invitation = group.groupinvitations.get(pk=invitation_id).delete()
    messages.success(request, _('Usunąłeś zaproszenie.'))
    return redirect('groups:show:invitations', group.pk)
