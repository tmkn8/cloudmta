from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib import messages
from django.utils.translation import ugettext as _
from .models import Character
from .forms import CreateCharacterForm, CharacterSettingsForm

@login_required
def characters_index(request):
    """Wyświetl wszystkie postacie użytkownika"""
    characters = request.user.characters.all()
    return render(request, 'characters/index.html', {'characters': characters})

@login_required
@user_passes_test(get_user_model().has_passed_rp_test, 'accounts:roleplay-test')
@user_passes_test(get_user_model().can_create_character,
    'characters:index')
def characters_create(request):
    """Stwórz postać"""
    if request.method == 'POST':
        form = CreateCharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.memberid = request.user
            character.save()
            return redirect('characters:show:index', pk=character.pk)
    else:
        form = CreateCharacterForm()
    return render(request, 'characters/create.html', {'form': form})

def get_character_object(request, pk):
    """Zwróć obiekt postaci

    Funkcja zapobiega powtarzaniu kodu do pobierania obiektu postaci.
    Zwraca kod HTTP 404, jeżeli użytkownik nie jest właścicielem postaci."""
    return get_object_or_404(Character, pk=pk, memberid=request.user)

@login_required
def characters_show_index(request, pk):
    """Pokaż główną zakładkę w szczegółach postaci"""
    character = get_character_object(request, pk)
    return render(request, 'characters/show/index.html',
        {'character': character})

@login_required
def characters_show_items(request, pk):
    """Pokaż przedmioty postaci"""
    character = get_character_object(request, pk)
    items = character.items
    return render(request, 'characters/show/items.html',
        {'character': character, 'items': items})

@login_required
def characters_show_vehicles(request, pk):
    """Pokaż pojazdy postaci"""
    character = get_character_object(request, pk)
    vehicles = character.vehicles
    return render(request, 'characters/show/vehicles.html',
        {'character': character, 'vehicles': vehicles})

@login_required
def characters_show_doors(request, pk):
    """Pokaż pojazdy postaci"""
    character = get_character_object(request, pk)
    doors = character.doors
    return render(request, 'characters/show/doors.html',
        {'character': character, 'doors': doors})


@login_required
def characters_show_groups(request, pk):
    """Pokaż pojazdy postaci"""
    character = get_character_object(request, pk)
    groups = character.groups.all()
    invitations = character.groupinvitations.all()
    return render(request, 'characters/show/groups.html',
        {'character': character, 'groups': groups,
        'invitations': invitations})

@login_required
def characters_show_settings(request, pk):
    """Pokaż ustawienia w szczegółach postaci"""
    character = get_character_object(request, pk)
    if request.method == 'POST':
        form = CharacterSettingsForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
    else:
        form = CharacterSettingsForm(instance=character)
    return render(request, 'characters/show/settings.html',
        {'character': character, 'form': form})

@login_required
def characters_show_group_invitations_accept(request, pk, invitation_id):
    """Akceptuj zaproszenie do grupy"""
    character = get_character_object(request, pk)
    invitation = get_object_or_404(character.groupinvitations, pk=invitation_id)
    # Czy gracz nie jest w za dużej ilości grup?
    if character.groupmembers.all().count() >= settings.RP_MAX_GROUP_NUMBER:
        messages.error(request, _("Przekroczyłeś limit ilości grup na postać: "
            "%d" % settings.RP_MAX_GROUP_NUMBER))
        return redirect('characters:show:groups', character.pk)

    # Czy gracz nie jest już w tej grupie obecnie?
    if character.groupmembers.filter(groupid=invitation.group).count():
        messages.error(request, _("Postać już obecnie jest w tej "
            "grupie."))
        return redirect('characters:show:groups', character.pk)

    invitation.group.add_new_member(character=character)
    invitation.delete()
    messages.success(request, _("Zostałeś dodany do grupy"))
    return redirect('characters:show:groups', character.pk)

@login_required
def characters_show_group_invitations_decline(request, pk, invitation_id):
    """Odrzuć zaproszenie do grupy"""
    character = get_character_object(request, pk)
    invitation = get_object_or_404(character.groupinvitations, pk=invitation_id)
    invitation.delete()
    messages.success(request, _("Skasowano zaproszenie do grupy"))
    return redirect('characters:show:groups', character.pk)
