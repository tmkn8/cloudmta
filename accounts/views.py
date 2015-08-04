from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import QuizQuestion, FriendRequest
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

def get_user_object(slug):
    return get_object_or_404(get_user_model(), username=slug)

def accounts_profile_index(request, slug):
    """Główna zakładka profili użytkownika"""
    user = get_user_object(slug)
    if request.is_ajax():
        template = 'accounts/profile/ajax/index.html'
    else:
        template = 'accounts/profile/index.html'
    return render(request, template, {'user': user})

def accounts_profile_about_me(request, slug):
    """Główna zakładka profili użytkownika"""
    user = get_user_object(slug)
    if request.is_ajax():
        template = 'accounts/profile/ajax/about_me.html'
    else:
        template = 'accounts/profile/about_me.html'
    return render(request, template, {'user': user})

def accounts_profile_characters(request, slug):
    """Główna zakładka profili użytkownika"""
    user = get_user_object(slug)
    if request.is_ajax():
        template = 'accounts/profile/ajax/characters.html'
    else:
        template = 'accounts/profile/characters.html'
    return render(request, template, {'user': user})

def accounts_profile_friends(request, slug):
    """Główna zakładka profili użytkownika"""
    user = get_user_object(slug)
    if request.is_ajax():
        template = 'accounts/profile/ajax/friends.html'
    else:
        template = 'accounts/profile/friends.html'
    return render(request, template, {'user': user})

def accounts_profile_logs(request, slug):
    """Główna zakładka profili użytkownika"""
    user = get_user_object(slug)
    if request.is_ajax():
        template = 'accounts/profile/ajax/logs.html'
    else:
        template = 'accounts/profile/logs.html'
    return render(request, template, {'user': user})

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
    context = {
        'invited_by': request.user.friends_invited_by.all(),
        'invited': request.user.friends_invited.all(),
    }
    return render(request, 'accounts/friends/requests.html', context)

def friends_send_request(request, friend_pk):
    """Strona wysyłania zaproszeń do znajomych

    Jeżeli przyjdzie GET, to wyślij zapytanie czy dodać znajomego."""
    friend = get_object_or_404(request.user.friends, pk=friend_pk)
    if request.method == 'POST':
        # Nie możesz dodać siebie do znajomych
        if request.user == friend:
            messages.error(request, _('Nie możesz dodać się do znajomych.'))
            return redirect(request.user.get_absolute_url())

        # Sprawdź czy użytkownicy są już znajomymi
        if request.user.friends.filter(pk=friend.pk).count():
            messages.error(request, _('Jesteś już znajomym tego użytkownika.'))
            return redirect('accounts:friends:requests')

        # Sprawdź czy istnieje zaproszenie do znajomych do/od tego użytkownika
        if FriendRequest.objects.filter(
                    Q(invited=request.user, invited_by=friend) |
                    Q(invited=friend, invited_by=request.user)
                ).count():
            messages.error(request, _('Obecnie istnieje zaproszenie do/od tego '
                'użytkownika.'))
            return redirect('accounts:friends:requests')

        # Wyślij zaproszenie do znajomych
        friend_request = FriendRequest(invited_by=request.user, invited=friend)
        friend_request.save()
        message.success(request, _("Wysłano prośbę o znajomość do %s" % friend))
        return redirect('accounts:friends:requests')
    return render(request, 'accounts/friends/send_request.html',
        {'friend': friend})

def friends_delete_request(request, pk):
    """Odrzuć lub usuń zaproszenie do znajomych"""
    friend_request = get_object_or_404(FriendRequest, pk=pk)
    if friend_request.delete_friend_request(user=request.user):
        if request.user == friend_request.invited:
            message = _("Zaproszenie od %s zostało odrzucone" %
                friend_request.invited_by)
        else:
            message = ("Zaproszenie wysłane do %s zostało usunięte" %
                friend_request.invited)
        messages.success(request, message)
    else:
        messages.error(request, _('Wystąpił błąd podczas usuwania zaproszenia. '
            'Spróbuj ponownie.'))
    return redirect('accounts:friends:requests')

def friends_accept_request(request, pk):
    """Akceptuj zaproszenie do znajomych"""
    friend_request = get_object_or_404(FriendRequest, pk=pk)
    if friend_request.accept_friend_request(user=request.user):
        messages.success(request, _("%s został Twoim znajomym." %
            friend_request.invited_by))
    else:
        messages.error(request, _('Wystąpił błąd podczas akceptowania zaproszenia. '
            'Spróbuj ponownie.'))
    return redirect('accounts:friends:requests')
