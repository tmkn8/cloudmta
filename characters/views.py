from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import get_user_model
from .models import Character
from .forms import CreateCharacterForm

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

    Funkcja zapobiega powtarzaniu kodu do pobierania obiektu postaci."""
    return get_object_or_404(Character, pk=pk, memberid=request.user.get_member_id())

def characters_show_index(request, pk):
    """Pokaż główną zakładkę w szczegółach postaci"""
    character = get_character_object(request, pk)
    return render(request, 'characters/show/index.html',
        {'character': character})

def characters_show_settings(request, pk):
    """Pokaż ustawienia w szczegółach postaci"""
    character = get_character_object(request, pk)
    return render(request, 'characters/show/settings.html',
        {'character': character})
