from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import get_user_model
from .forms import CreateCharacterForm

@login_required
def characters_index(request):
    """Wyświetl wszystkie postacie użytkownika"""
    characters = Character.objects.all(memberid=request.user.pk)
    return render(request,)

@user_passes_test(get_user_model().can_create_character)
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
