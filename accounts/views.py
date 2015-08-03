from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import QuizQuestion
from .forms import LoginForm

def has_not_passed_rp_test(user):
    """Dekorator sprawdzający czy użytkownik nie zdał testu RP"""
    return not user.has_passed_rp_test()

def accounts_login(request):
    """Strona logowania"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        form = LoginForm(request.POST)
        if user is not None:
            login(request, user)
            messages.success(request, _('Zalogowanie przebiegło poprawnie.'))
            return redirect('homepage')
        else:
            messages.error(request, _('Podałeś nieprawidłowe dane'))
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def accounts_logout(request):
    """Strona wylogowywania"""
    logout(request)
    messages.success(request, _('Nastąpiło poprawne wylogowanie.'))
    return redirect('homepage')

def accounts_register(request):
    """Przekieruj użytkownika na rejestrację konta na stronie MyBB"""
    return redirect(settings.FORUM_REGISTER_ACCOUNT_LINK)

@login_required
@user_passes_test(has_not_passed_rp_test, 'characters:index')
def roleplay_test(request):
    """Test RP, który użytkownik musi zdać, aby założyć postać"""
    if request.method == 'POST':
        for i in range(0, settings.RP_TEST_QUESTIONS_NUMBERS):
            question_id = request.POST.get('id_' + str(i), None)
            answer = request.POST.get('answer_' + str(i), None)
            question = QuizQuestion.objects.get(pk=question_id)
            if not question.is_valid_answer(answer):
                messages.error(request, _('Udzieliłeś niepoprawnej odpowiedzi. '
                    'Spróbuj ponownie.'))
                return redirect('accounts:roleplay-test')

        request.user.pass_rp_test()
        messages.success(request, _('Gratulujemy zdania testu z wiedzy '
            'roleplay. Możesz teraz przystąpić do stworzenia postaci.'))
        return redirect('characters:index')
    else:
        questions = QuizQuestion.objects.all().order_by('?')[:settings.RP_TEST_QUESTIONS_NUMBERS]
        if len(questions) < settings.RP_TEST_QUESTIONS_NUMBERS:
            raise Exception(_("Nie wystarczająco pytań w systemie."))
        questions_indices = range(0, settings.RP_TEST_QUESTIONS_NUMBERS)
    return render(request, 'accounts/roleplay_test.html',
        {'questions': zip(questions_indices, questions)})

def accounts_profile_index(request, slug):
    """Główna zakładka profili użytkownika"""
    user = get_object_or_404(getappen_user_model(), username=slug)
    return render(request, 'accounts/profile/index.html', {'user': user})

@login_required
def friends_index(request):
    """Wyświetl listę znajomych użytkownika"""
    friends = request.user.friends.all()
    return render(request, 'accounts/friends/index.html', {'friends': friends})

@login_required
def friends_delete_friend(request, friend_pk):
    """Strona kasacji znajomego

    Jeżeli przyjdzie GET, to wyślij zapytanie czy skasować znajomego."""
    friend = get_object_or_404(request.user.friends, pk=friend_pk)
    if request.method == 'POST':
        request.user.friends.remove(friend)
        messages.success(request, _("Pomyślnie skasowałeś znajomego %s"
            % friend))
        return redirect('accounts:friends:index')
    return render(request, 'accounts/friends/delete_friend.html',
        {'friend': friend})

def friends_requests(request):
    pass

def friends_send_request(request, friend_pk):
    """Strona wysyłania zaproszeń do znajomych

    Jeżeli przyjdzie GET, to wyślij zapytanie czy dodać znajomego."""
    friend = get_object_or_404(request.user.friends, pk=friend_pk)
    if request.method == 'POST':
        request.user.friends.delete(friend)
        messages.success(request, _("Pomy znajomego %s"
            % friend))
        return redirect('accounts:friends:index')
    return render(request, 'accounts/friends/send_request.html',
        {'friend': friend})

def friends_delete_request(request, pk):
    pass

def friends_accept_request(request, pk):
    pass
