from django.db import models
from django.db.models import Q
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import UserManager
from characters.models import Character
import hashlib
import urllib
from gravatar import Gravatar
from django.templatetags.static import static

class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_VALIDATOR = RegexValidator(r'^([A-Za-z0-9]{3,})$')
    username = models.CharField(verbose_name=_('nazwa użytkownika'),
        max_length=20, validators=[USERNAME_VALIDATOR], unique=True)
    email = models.EmailField(verbose_name=_('adres e-mail'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    is_active = models.BooleanField(default=True, verbose_name=_('czy konto '
        'jest aktywne'))
    is_staff = models.BooleanField(default=False, verbose_name=_('ekipa'),
        help_text=_('ma dostęp do strony administracji.'))
    date_joined = models.DateTimeField(_('data dołączenia'),
        default=timezone.now)
    avatar = models.ImageField(verbose_name=_('awatar'), blank=True, null=True,
        upload_to='user-avatars')
    cover_photo = models.ImageField(verbose_name=_('okładka profilu'),
        upload_to='cover_photos', blank=True, null=True)
    passed_rp_test = models.BooleanField(default=False, verbose_name=_('zdał '
        'test RP'))
    friends = models.ManyToManyField('self', verbose_name=_('znajomi'))
    about_me = models.TextField(verbose_name=_('o mnie'),
        help_text=_('markdown'), blank=True, null=True)
    public_email = models.BooleanField(verbose_name=_('adres e-mail '
        'widoczny publicznie'), default=False)
    skype_id = models.CharField(max_length=40, verbose_name=_('identyfikator '
        'skype'), null=True, blank=True)

    objects = UserManager()

    def __str__(self):
        """Zwróć nazwę użytkownika"""
        return self.username

    class Meta:
        verbose_name = _('użytkownik Django')
        verbose_name_plural = _('użytkownicy Django')

    def get_absolute_url(self):
        """Pobierz link do profilu"""
        return reverse('accounts:profile:index', kwargs={'slug': self.username})

    def get_cover_photo_url(self):
        """Zwróć URL cover photo"""
        if self.cover_photo:
            return self.cover_photo.url
        return None

    def get_avatar_url(self):
        """Zwróc URL awatara"""
        if self.avatar:
            return self.avatar.url

        gravatar = Gravatar(self.email.lower())
        gravatar.size = 300
        gravatar.default = 404
        try:
            gravatar_url = urllib.request.urlopen(gravatar.thumb)
        except urllib.error.URLError:
            return static(settings.DEFAULT_AVATAR)
        return gravatar.thumb

    def format_about_me(self):
        if not self.about_me:
            return None
        import markdown
        return markdown.markdown(self.about_me, safe_mode=True)

    def mybbmember(self):
        """Pobierz obiekt użytkownika forum"""
        return MyBBMember.objects.get(pk=self.pk)

    def get_full_name(self):
        """Wymagane przez klasę rodzica"""
        return self

    def get_short_name(self):
        """Wymagane przez klasę rodzica"""
        return self

    def can_create_character(self):
        """Sprawdź czy użytkownik może stworzyć postać"""
        if not self.is_authenticated():
            return False
        if not self.has_passed_rp_test():
            return False
        if self.characters.filter(
                    Q(onlinetime__lte=settings.RP_MIN_CHARACTER_TIME),
                    Q(blocked=False),
                    Q(memberid=self)
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

class MyBBMember(models.Model):
    """Ten model jest tabelą z MyBB, na cele logowania"""
    uid = models.AutoField(primary_key=True, verbose_name=_('UID'))
    username = models.CharField(max_length=120, verbose_name=_('Nazwa '
        'użytkownika'))
    email = models.EmailField(max_length=220, verbose_name=_('Adres e-mail'))
    password = models.CharField(max_length=120, verbose_name=_('Hasło'),
        editable=False)
    salt = models.CharField(max_length=10, verbose_name=_('Sól'),
        editable=False)

    def __str__(self):
        return self.username

    class Meta:
        managed = False # Django nie dodaje tabeli w bazie
        db_table ='mybb_users'
        verbose_name = _('użytkownik forum')
        verbose_name_plural = _('użytkownicy forum')

    def get_django_user_model(self):
        """Znajdź model użytkownika w Django"""
        return self.save_django_user()

    def save_django_user(self):
        """Funkcja pobiera użytkownika Django powiązanego z użytkownikiem MyBB
        i aktualizuje podany email oraz nazwę użytkownika lub tworzy nowy model.
        """
        user, created = get_user_model().objects.get_or_create(pk=self.pk)
        if created == True:
            user.id = self.pk
            user.save()
        if user.email != self.email or user.username != self.username:
            user.email = self.email
            user.username = self.username
            user.save()
        return user

    def check_password(self, password=None):
        """Sprawdza hasło algorytmem MyBB"""
        member_salt_hash = hashlib.md5(self.salt.encode('utf-8')).hexdigest()
        input_password = hashlib.md5(password.encode('utf-8')).hexdigest()
        hashed_password = hashlib.md5(member_salt_hash.encode('utf-8') \
            + input_password.encode('utf-8'))
        if hashed_password.hexdigest() == self.password:
            return True
        return False

class QuizQuestion(models.Model):
    """Model przechowuje pytania do testu RP"""
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
        choices=CORRECT_ANSWER_CHOICES, verbose_name=_('poprawna odpowiedź'))

    def __str__(self):
        return _("Pytanie %s..." % self.question[:10])

    class Meta:
        verbose_name = _('pytanie z testu wiedzy RP')
        verbose_name_plural = _('pytania z testu wiedzy RP')

    def is_valid_answer(self, answer):
        """Sprawdź czy podana odpowiedź jest poprawna."""
        if not isinstance(answer, str):
            return False
        if self.correct_answer.lower() == answer.lower():
            return True
        return False

class FriendRequest(models.Model):
    invited_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name=_('zapraszający'), related_name='friends_invited_by',
        related_query_name='friend_invited_by')
    invited = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name=_('zaproszony użytkownik'), related_name='friends_invited',
        related_query_name='friend_invited')
    sent_time = models.DateTimeField(verbose_name=_('czas zaproszenia'),
        auto_now_add=True)

    def __str__(self):
        return _("%s zaproszony przez %s" % (self.invited, self.invited_by))

    class Meta:
        verbose_name = _('zaproszenie do znajomych')
        verbose_name_plural = _('zaproszenia do znajomych')

    def accept_friend_request(self, user):
        """Akceptuj zaproszenie do znajomych"""
        # Jeżeli użytkownik nie jest zaproszony, to nie pozwól mu przyjąć
        # zaproszenia
        if user != self.invited:
            return False
        # Dodaj znajomego
        user.friends.add(self.invited_by)
        # Skasuj zaproszenie
        self.delete()
        return True

    def delete_friend_request(self, user):
        """Odrzuć lub usuń zaproszenie do znajomych"""
        if user == self.invited or user == self.invited_by:
            self.delete()
            return True
        return False
