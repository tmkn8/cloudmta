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
    id = models.AutoField(db_column='ID', primary_key=True)
    memberid = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name=_('Konto'), related_name='characters',
        related_query_name='character')
    NAME_VALIDATOR =  NAME_VALIDATOR = RegexValidator(r'^([A-Za-z]{2,})([\s][A-Za-z]{2,})?([\s][A-Za-z]{2,})$')
    name = models.CharField(max_length=22, validators=[NAME_VALIDATOR],
        verbose_name=_('Imię i nazwisko'), help_text=_('Drugie imię opcjonalne,'
        ' odstępy rozdzielać spacją.'), unique=True)

    def generate_facecode():
        while True:
            facecode = ''
            for i in range(6):
                facecode += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789').upper()
            if not Character.objects.filter(facecode=facecode).count():
                return facecode
    facecode = models.CharField(db_column='faceCode', default=generate_facecode,
        verbose_name=_('Kod twarzy'), max_length=6, unique=True)

    def generate_shortdna_code():
        while True:
            shortdna = ''
            for i in range(4):
                shortdna += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789').lower()
            if not Character.objects.filter(shortdna=shortdna).count():
                return shortdna
    shortdna = models.CharField(db_column='shortDNA', max_length=4, unique=True,
        verbose_name=_('Krótki kod DNA'), help_text=_('Używany m.in. do '
        'kominiarek'), default=generate_shortdna_code)

    def generate_dna_code():
        while True:
            random_number = str(random.getrandbits(128))
            dna = hashlib.md5(random_number.encode('utf-8')).hexdigest().upper()
            if not Character.objects.filter(dna=dna).count():
                return dna
    dna = models.CharField(db_column='DNA', max_length=255, unique=True,
        verbose_name=_('DNA'), default=generate_dna_code)
    hp = models.FloatField(default=100, verbose_name=_('Punkty życia'))
    skin = models.PositiveSmallIntegerField(default=1,
        verbose_name=_('ID Skina'))
    x = models.FloatField(blank=True, null=True, verbose_name=_('Pozycja X'))
    y = models.FloatField(blank=True, null=True, verbose_name=_('Pozycja Y'))
    z = models.FloatField(blank=True, null=True, verbose_name=_('Pozycja Z'))
    angle = models.FloatField(blank=True, null=True, verbose_name=_('Kąt'))
    dimension = models.PositiveIntegerField(default=0, verbose_name=_('Wymiar'))
    interior = models.PositiveIntegerField(default=0, verbose_name=_('Wnętrze'))
    money = models.PositiveIntegerField(default=settings.RP_DEFAULT_CHARACTER_MONEY,
        verbose_name=_('Gotówka'))
    bwtime = models.PositiveIntegerField(db_column='bwTime', default=0,
        verbose_name=_('Czas BW'), help_text=_('W sekundach'))
    ajtime = models.PositiveIntegerField(db_column='ajTime', default=0,
        verbose_name=_('Czas AJ'), help_text=_('W sekundach'))
    onlinetime = models.PositiveIntegerField(db_column='onlineTime', default=0,
        verbose_name=_('Czas w grze'), help_text=_('W sekundach'))
    afktime = models.PositiveIntegerField(db_column='afkTime', default=0,
        verbose_name=_('Czas AFK'), help_text=_('W sekundach'))
    SEX_CHOICES = (
        (1, _('Mężczyzna')),
        (2, _('Kobieta')),
    )
    sex = models.PositiveSmallIntegerField(choices=SEX_CHOICES,
        verbose_name=_('Płeć'))
    ingame = models.BooleanField(db_column='inGame', verbose_name=_('Postać w '
        'grze'), default=False)
    lastvisit = UnixDateTimeField(db_column='lastVisit',
        verbose_name=_('Ostatnia wizyta'), null=True, blank=True)
    blocked = models.BooleanField(default=False, verbose_name=_('Zablokowana'))
    hide = models.BooleanField(default=False, verbose_name=_('Ukryta'))
    dob = models.DateField(verbose_name=_('Data urodzenia'))
    activated = models.BooleanField(default=False, verbose_name=_('Aktywowana'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('characters:show:index', kwargs={'pk': self.pk})

    class Meta:
        db_table = '_characters'
        verbose_name = _('postać')
        verbose_name_plural = _('postacie')

    def get_skin_static_url(self):
        return "%s/%d.%s" % (settings.RP_SKINS_STATIC_DIRECTORY,
            self.skin, settings.RP_SKINS_IMG_FORMAT)

    def format_onlinetime(self):
        seconds = self.onlinetime
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return "%dh %02dmin." % (h, m)

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
    skin_id = models.PositiveSmallIntegerField(verbose_name=_('ID skina'), unique=True)
    SEX_CHOICES = (
        (1, _('Mężczyzna')),
        (2, _('Kobieta')),
    )
    sex = models.PositiveSmallIntegerField(choices=SEX_CHOICES,
        verbose_name=_('Płeć'))

    def __str__(self):
        return _("Startowy skin %d (%s)" % (self.skin_id, self.get_sex_display()[0]))

    class Meta:
        verbose_name = _('skin startowy')
        verbose_name_plural = _('skiny startowe')

class Facecode(models.Model):
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
