from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import get_user_model
from .models import Character
from .forms import CreateCharacterForm, CharacterSettingsForm

@login_required
def characters_index(request):
    """Wyświetl wszystkie postacie użytkownika"""
    characters = Character.objects.filter(memberid=request.user.member_id)
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
            character.memberid = request.user.get_member_id()
            character.save()
            return redirect('characters:show:index', pk=character.pk)
    else:
        form = CreateCharacterForm()
    return render(request, 'characters/create.html', {'form': form})

def get_character_object(request, pk):
    """Zwróć obiekt postaci

    Funkcja zapobiega powtarzaniu kodu do pobierania obiektu postaci.
    Zwraca kod HTTP 404, jeżeli użytkownik nie jest właścicielem postaci."""
    return get_object_or_404(Character, pk=pk, memberid=request.user.get_member_id())

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
def characters_show_groups(request, pk):
    """Pokaż pojazdy postaci"""
    character = get_character_object(request, pk)
    groups = character.groups.all()
    return render(request, 'characters/show/groups.html',
        {'character': character, 'groups': groups})

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
