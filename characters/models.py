import random
import datetime
import hashlib
from django.db import models
from django.utils.translation import ugettext as _
from django_unixdatetimefield import UnixDateTimeField
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
from django.db.models import get_model

class Character(models.Model):
    """Model przechowujący informacje o postaciach"""
    id = models.AutoField(db_column='ID', primary_key=True)
    memberid = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name=_('konto'), related_name='characters',
        related_query_name='character')
    NAME_VALIDATOR =  NAME_VALIDATOR = RegexValidator(r'^([A-Za-z]{2,})([\s][A-Za-z]{2,})?([\s][A-Za-z]{2,})$')
    name = models.CharField(max_length=22, validators=[NAME_VALIDATOR],
        verbose_name=_('imię i nazwisko'), help_text=_('drugie imię opcjonalne,'
        ' odstępy rozdzielać spacją.'), unique=True)

    def generate_facecode():
        """Generuje kod twarzy

        Gdy postać jest tworzona, wygeneruj losowy ciąg znaków
        i sprawdź jego unikalność w bazie danych."""
        while True:
            facecode = ''
            for i in range(6):
                facecode += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789').upper()
            if not Character.objects.filter(facecode=facecode).count():
                return facecode
    facecode = models.CharField(db_column='faceCode', default=generate_facecode,
        verbose_name=_('kod twarzy'), max_length=6, unique=True)

    def generate_shortdna_code():
        """Generuje krótki kod DNA i sprawdza jego unikalność"""
        while True:
            shortdna = ''
            for i in range(4):
                shortdna += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789').lower()
            if not Character.objects.filter(shortdna=shortdna).count():
                return shortdna
    shortdna = models.CharField(db_column='shortDNA', max_length=4, unique=True,
        verbose_name=_('krótki kod DNA'), help_text=_('używany m.in. do '
        'kominiarek'), default=generate_shortdna_code)

    def generate_dna_code():
        """Generuje kod DNA i sprawdza jego unikalność"""
        while True:
            random_number = str(random.getrandbits(128))
            dna = hashlib.md5(random_number.encode('utf-8')).hexdigest().upper()
            if not Character.objects.filter(dna=dna).count():
                return dna
    dna = models.CharField(db_column='DNA', max_length=255, unique=True,
        verbose_name=_('DNA'), default=generate_dna_code)
    hp = models.FloatField(default=100, verbose_name=_('punkty życia'))
    skin = models.PositiveSmallIntegerField(default=1,
        verbose_name=_('ID Skina'))
    x = models.FloatField(blank=True, null=True, verbose_name=_('pozycja X'))
    y = models.FloatField(blank=True, null=True, verbose_name=_('pozycja Y'))
    z = models.FloatField(blank=True, null=True, verbose_name=_('pozycja Z'))
    angle = models.FloatField(blank=True, null=True, verbose_name=_('kąt'))
    dimension = models.PositiveIntegerField(default=0, verbose_name=_('wymiar'))
    interior = models.PositiveIntegerField(default=0, verbose_name=_('wnętrze'))
    money = models.PositiveIntegerField(default=settings.RP_DEFAULT_CHARACTER_MONEY,
        verbose_name=_('gotówka'))
    bwtime = models.PositiveIntegerField(db_column='bwTime', default=0,
        verbose_name=_('czas BW'), help_text=_('w sekundach'))
    ajtime = models.PositiveIntegerField(db_column='ajTime', default=0,
        verbose_name=_('czas AJ'), help_text=_('w sekundach'))
    onlinetime = models.PositiveIntegerField(db_column='onlineTime', default=0,
        verbose_name=_('czas w grze'), help_text=_('w sekundach'))
    afktime = models.PositiveIntegerField(db_column='afkTime', default=0,
        verbose_name=_('czas AFK'), help_text=_('w sekundach'))
    SEX_CHOICES = (
        (1, _('Mężczyzna')),
        (2, _('Kobieta')),
    )
    sex = models.PositiveSmallIntegerField(choices=SEX_CHOICES,
        verbose_name=_('płeć'))
    ingame = models.BooleanField(db_column='inGame', verbose_name=_('postać w '
        'grze'), default=False)
    lastvisit = UnixDateTimeField(db_column='lastVisit',
        verbose_name=_('ostatnia wizyta'), null=True, blank=True)
    blocked = models.BooleanField(default=False, verbose_name=_('zablokowana'))
    hide = models.BooleanField(default=False, verbose_name=_('ukryta'))
    dob = models.DateField(verbose_name=_('data urodzenia'))
    activated = models.BooleanField(default=True, verbose_name=_('aktywowana'),
        help_text=_('stare, nie tykać'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Link do panelu postaci"""
        return reverse('characters:show:index', kwargs={'pk': self.pk})

    class Meta:
        db_table = '_characters'
        verbose_name = _('postać')
        verbose_name_plural = _('postacie')

    def get_skin_static_url(self):
        """Pobierz link do skinu użycia w {% static %}"""
        return "%s/%d.%s" % (settings.RP_SKINS_STATIC_DIRECTORY,
            self.skin, settings.RP_SKINS_IMG_FORMAT)

    @staticmethod
    def format_time(seconds):
        """Formatuj czas z sekund do godzin i minut"""
        seconds = int(seconds)
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return "%dh %02dmin" % (h, m)

    def format_online_time(self):
        """Sformatuj czas online"""
        return self.format_time(self.onlinetime)

    def format_afk_time(self):
        """Sformatuj czas AFK"""
        return self.format_time(self.afktime)

    def format_bw_time(self):
        """Sformatuj czas BW"""
        return self.format_time(self.bwtime)

    def format_aj_time(self):
        """Sformatuj czas AJ"""
        return self.format_time(self.ajtime)

    def items(self):
        """Pobierz obiekty przedmiotów tej postaci"""
        return get_model('items', 'Item').objects.filter(owner=self.pk,
            ownertype=settings.RP_ITEM_OWNER_TYPE_ID_CHARACTER)

    def vehicles(self):
        """Pobierz pojazdy postaci"""
        return get_model('vehicles', 'Vehicle').objects.filter(ownerid=self.pk,
            ownertype=settings.RP_VEHICLE_OWNER_TYPE_ID_CHARACTER)

    def doors(self):
        """Pobierz drzwi postaci"""
        return get_model('doors', 'Door').objects.filter(owner=self.pk,
            ownertype=settings.RP_DOOR_OWNER_TYPE_ID_CHARACTER)

class StartSkin(models.Model):
    """Przechowuje informacje o skinach dostępnych przy tworzeniu postaci"""
    skin_id = models.PositiveSmallIntegerField(verbose_name=_('ID skina'), unique=True)
    SEX_CHOICES = (
        (1, _('mężczyzna')),
        (2, _('kobieta')),
    )
    sex = models.PositiveSmallIntegerField(choices=SEX_CHOICES,
        verbose_name=_('płeć'))

    def __str__(self):
        return _("Startowy skin %d (%s)" % (self.skin_id, self.get_sex_display()[0]))

    class Meta:
        verbose_name = _('skin startowy')
        verbose_name_plural = _('skiny startowe')

    def get_static_url(self):
        """Pobierz link do skinu do użycia w {% static %}"""
        return "%s/%d.%s" % (settings.RP_SKINS_STATIC_DIRECTORY,
            self.skin_id, settings.RP_SKINS_IMG_FORMAT)

class Facecode(models.Model):
    """Model zawiera informacje o aliasach nadanych dla innych postaci"""
    charid = models.ForeignKey('Character', db_column='charID',
        verbose_name=_('Postać'), related_name='facecodes')
    facecode = models.CharField(db_column='faceCode', max_length=10,
        verbose_name=_('Kod twarzy'), help_text=_('Kod twarzy postaci, do '
        'której przypisany jest alias.'))
    name = models.CharField(max_length=100, verbose_name=_('Alias postaci'))

    class Meta:
        db_table = '_faceCodes'
        verbose_name = _('kod twarzy')
        verbose_name_plural = _('kody twarzy')

class LoginLog(models.Model):
    """Przechowuje logi logowania użytkownika"""
    id = models.AutoField(db_column='ID', primary_key=True)
    charid = models.ForeignKey('Character', db_column='charID',
        verbose_name=_('postać'))
    ip = models.GenericIPAddressField(verbose_name=_('adres IP'),
        default='127.0.0.1')
    serial = models.CharField(blank=True, null=True, verbose_name=_('serial'),
        max_length=settings.RP_SERIAL_LENGTH)
    time = UnixDateTimeField(verbose_name=_('data logowania'), blank=True,
        null=True)

    def __str__(self):
        return _("%s (%s)" % (self.charid, self.serial))

    class Meta:
        db_table = '_login_logs'
        verbose_name = _('log logowania')
        verbose_name_plural = _('logi logowania')

class PenaltyLog(models.Model):
    """Logi kar"""
    id = models.AutoField(db_column='ID', primary_key=True)
    serial = models.CharField(max_length=settings.RP_SERIAL_LENGTH,
        verbose_name=_('serial'))
    ip = models.GenericIPAddressField(verbose_name=_('adres IP'))
    character = models.ForeignKey('characters.Character',
        verbose_name=_('postać'), db_column='userID',
        related_name='characters', related_query_name='character')
    admin = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name=_('administrator'), db_column='adminID',
        related_name='admins', related_query_name='admin')
    reason = models.TextField(verbose_name=_('powód'), blank=True, null=True)
    time = UnixDateTimeField(verbose_name=_('data nadania'))
    expire = UnixDateTimeField(verbose_name=_('data wygaśnięcia'), blank=True,
        null=True)
    TYPE_CHOICES = (
        (1, _('kick')),
        (2, _('admin jail')),
        (3, _('warn')),
        (4, _('ban')),
        (5, _('blokada postaci')),
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=1,
        verbose_name=_('typ kary'))

    def __str__(self):
        return "%s dla %s" % (self.get_type_display, self.character)

    class Meta:
        db_table = '_penalty_logs'
        verbose_name = _('informacje o karze')
        verbose_name_plural = _('logi kar')
