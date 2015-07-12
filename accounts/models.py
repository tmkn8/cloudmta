from django.db import models
from django.db.models import Q
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _
from characters.models import Character
import hashlib

class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_VALIDATOR = RegexValidator(r'^([A-Za-z0-9]{3,})$')
    username = models.CharField(verbose_name=_('Nazwa użytkownika'),
        max_length=20, validators=[USERNAME_VALIDATOR], unique=True,
        editable=False)
    email = models.EmailField(verbose_name=_('Adres e-mail'), unique=True,
        editable=False)
    USERNAME_FIELD = 'email'
    member_id = models.IntegerField(verbose_name=_('ID konta '
        'na forum'), unique=True, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    passed_rp_test = models.BooleanField(default=False)

    def member(self):
        """Pobierz obiekt użytkownika forum"""
        return Member.objects.get(pk=self.member_id)

    def characters(self):
        """Pobierz postacie użytkownika"""
        return Character.objects.filter(memberid=self.member_id)

    def __str__(self):
        """Zwróć nazwę użytkownika"""
        return self.username

    def get_full_name(self):
        """Wymagane przez rodzica"""
        return self

    def get_short_name(self):
        """Wymagane przez rodzica"""
        return self

    def get_member_id(self):
        """Pobierz ID konta z forum"""
        return self.member_id

    def can_create_character(self):
        """Sprawdź czy użytkownik może stworzyć postać"""
        if not self.is_authenticated():
            return False
        if not self.has_passed_rp_test():
            return False
        if self.characters().filter(
                    Q(onlinetime__lte=settings.RP_MIN_CHARACTER_TIME),
                    Q(blocked=False),
                    Q(memberid=self.member_id)
                ).count():
            return False
        return True

    def has_passed_rp_test(self):
        """Czy użytkownik zdał test RP"""
        return self.passed_rp_test

    def pass_rp_test(self):
        """Zdaj test RP gracza"""
        self.passed_rp_test = True
        self.save()

    class Meta:
        verbose_name = _('użytkownik Django')
        verbose_name_plural = _('użytkownicy Django')

class Member(models.Model):
    """Ten model jest tabelą z MyBB"""
    uid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=120)
    email = models.EmailField(max_length=220)
    password = models.CharField(max_length=120)
    salt = models.CharField(max_length=10)

    def get_django_user_model(self):
        """Znajdź model użytkownika w Django"""
        return self.save_django_user()

    def save_django_user(self):
        """Funkcja pobiera użytkownika Django powiązanego z użytkownikiem MyBB
        i aktualizuje podany email oraz nazwę użytkownika lub tworzy nowy model.
        """
        user, created = get_user_model().objects.get_or_create(member_id=self.pk)
        changed = False
        if user.email != self.email:
            user.email = self.email
            changed = True
        if user.username != self.username:
            user.username = self.username
            changed = True
        if changed:
            user.save()
        return user

    def check_password(self, password=None):
        """Sprawdza hasło algorytmem MyBB"""
        member_salt_hash = hashlib.md5(self.salt.encode('utf-8')).hexdigest()
        input_password = password.encode('utf-8')
        hashed_password = hashlib.md5(member_salt_hash.encode('utf-8') + input_password)
        if hashed_password.hexdigest() == self.password:
            return True
        return False

    class Meta:
        managed = False
        db_table ='mybb_users'
        verbose_name = _('użytkownik forum')
        verbose_name_plural = _('użytkownicy forum')

class QuizQuestion(models.Model):
    question = models.CharField(max_length=200, verbose_name=_('Pytanie'))
    answer_a = models.CharField(max_length=200, verbose_name=_('Odpowiedź A'))
    answer_b = models.CharField(max_length=200, verbose_name=_('Odpowiedź B'))
    answer_c = models.CharField(max_length=200, verbose_name=_('Odpowiedź C'))
    answer_d = models.CharField(max_length=200, verbose_name=_('Odpowiedź D'))
    CORRECT_ANSWER_CHOICES = (
        ('a', _('Odpowiedź A')),
        ('b', _('Odpowiedź B')),
        ('c', _('Odpowiedź C')),
        ('d', _('Odpowiedź D')),
    )
    correct_answer = models.CharField(max_length=1,
        choices=CORRECT_ANSWER_CHOICES)

    def __str__(self):
        return _("Pytanie %s..." % self.question[:10])

    def is_valid_answer(self, answer):
        """Sprawdź czy podana odpowiedź jest poprawna."""
        if not isinstance(answer, str):
            return False
        if self.correct_answer.lower() == answer.lower():
            return True
        return False

    class Meta:
        verbose_name = _('pytanie z testu wiedzy RP')
        verbose_name_plural = _('pytania z testu wiedzy RP')
