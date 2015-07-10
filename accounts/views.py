from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import QuizQuestion

def has_not_passed_rp_test(user):
    return not user.has_passed_rp_test()

@login_required
@user_passes_test(has_not_passed_rp_test, 'characters:index')
def roleplay_test(request):
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
