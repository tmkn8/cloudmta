from django.db import models
from django.utils.translation import ugettext as _
from django_unixdatetimefield import UnixDateTimeField
from django.conf import settings

class Character(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)
    memberid = models.BigIntegerField(db_column='memberID', db_index=True,
        verbose_name=_('ID użytkownika'))
    name = models.CharField(max_length=20, verbose_name=_('Imię'))
    lastname = models.CharField(max_length=20, verbose_name=_('Nazwisko'))
    facecode = models.CharField(db_column='faceCode',
        verbose_name=_('Kod twarzy'), max_length=6, unique=True)
    shortdna = models.CharField(db_column='shortDNA', max_length=4, unique=True,
        verbose_name=_('Krótki kod DNA'), help_text=_('Używany m.in. do '
        'kominiarek'))
    dna = models.CharField(db_column='DNA', max_length=255, unique=True,
        verbose_name=_('DNA'))
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
        'grze'))
    lastvisit = UnixDateTimeField(db_column='lastVisit',
        verbose_name=_('Ostatnia wizyta'))
    blocked = models.BooleanField(default=False, verbose_name=_('Zablokowana'))
    hide = models.BooleanField(default=False, verbose_name=_('Ukryta'))
    dob = models.DateField(verbose_name=_('Data urodzenia'))
    activated = models.BooleanField(default=False, verbose_name=_('Aktywowana'))

    def __str__(self):
        return "%s %s" % (self.name, self.lastname)

    class Meta:
        db_table = '_characters'
        verbose_name = _('Postać')
        verbose_name_plural = _('Postacie')
