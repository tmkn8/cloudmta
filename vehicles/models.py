from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.translation import ugettext as _
from jsonfield import JSONField
from django.apps import apps


class Vehicle(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True,
        verbose_name=_('ID pojazdu'))
    name = models.CharField(max_length=50, verbose_name=_('Nazwa pojazdu'))
    OWNER_TYPE_CHOICES = (
        (settings.RP_VEHICLE_OWNER_TYPE_ID_NONE, _('Brak')),
        (settings.RP_VEHICLE_OWNER_TYPE_ID_CHARACTER, _('Postać')),
        (settings.RP_VEHICLE_OWNER_TYPE_ID_GROUP, _('Grupa')),
    )
    ownertype = models.PositiveSmallIntegerField(db_column='ownerType',
        verbose_name=_('Typ właściciela'), choices=OWNER_TYPE_CHOICES)
    ownerid = models.IntegerField(db_column='ownerID', default=0,
        verbose_name=_('Właściciel'), help_text=_('ID właściciela'))
    c1r = models.PositiveSmallIntegerField(verbose_name=_('Kolor 1 R'),
        default=0, help_text=_('Wprowadź kolor w formacie RGB'))
    c1g = models.PositiveSmallIntegerField(verbose_name=_('Kolor 1 G'),
        default=0, help_text=_('Wprowadź kolor w formacie RGB'))
    c1b = models.PositiveSmallIntegerField(verbose_name=_('Kolor 1 B'),
        default=0, help_text=_('Wprowadź kolor w formacie RGB'))
    c2r = models.PositiveSmallIntegerField(verbose_name=_('Kolor 2 R'),
        default=0, help_text=_('Wprowadź kolor w formacie RGB'))
    c2g = models.PositiveSmallIntegerField(verbose_name=_('Kolor 2 G'),
        default=0, help_text=_('Wprowadź kolor w formacie RGB'))
    c2b = models.PositiveSmallIntegerField(verbose_name=_('Kolor 2 B'),
        default=0, help_text=_('Wprowadź kolor w formacie RGB'))
    model = models.PositiveSmallIntegerField(verbose_name=_('Model'),
        help_text=_('ID modelu pojazud w MTA'))
    hp = models.FloatField(verbose_name=_('Stan pojazdu'), default=0,
        help_text=_('Punkty życia pojazdu 0-1000'))
    spawned = models.BooleanField(default=False, verbose_name=_('Zespawnowany'))
    locked = models.BooleanField(default=True, verbose_name=_('Zamknięty'))
    x = models.FloatField(default=0, verbose_name=_('Pozycja X'))
    y = models.FloatField(default=0, verbose_name=_('Pozycja Y'))
    z = models.FloatField(default=0, verbose_name=_('Pozycja Z'))
    rx = models.FloatField(default=0, verbose_name=_('Rotacja X'))
    ry = models.FloatField(default=0, verbose_name=_('Rotacja Y'))
    rz = models.FloatField(default=0, verbose_name=_('Rotacja Z'))
    v1 = models.IntegerField(default=0)
    v2 = models.IntegerField(default=0)
    fuel = models.FloatField(default=20, verbose_name=_('Paliwo'),
        help_text=_('Ilość paliwa w baku'))
    maxfuel = models.PositiveSmallIntegerField(verbose_name=_('Pojemność baku'),
        default=50)
    damage = JSONField(blank=True, null=True, verbose_name=_('Zniszczenie '
        'pojazdu'), help_text=_('Szczegółowe zniszczenie poszczególnych części '
        'pojazdu'))
    interior = models.PositiveIntegerField(default=0, verbose_name=_('Wnętrze'))
    dimension = models.PositiveIntegerField(default=0, verbose_name=_('Wymiar'))
    FLASHTYPE_CHOICES = (
        (0, _('Brak')),
        (1, _('Światła PD')),
        (2, _('Światła FD')),
    )
    flashtype = models.PositiveIntegerField(db_column='flashType', default=0,
        verbose_name=_('Typ świateł emergency'), choices=FLASHTYPE_CHOICES)
    distance = models.FloatField(default=0, verbose_name=_('Przebieg'))
    hasalarm = models.BooleanField(db_column='hasAlarm', default=False,
        verbose_name=_('Alarm'))
    handbrake = models.BooleanField(default=True, verbose_name=_('Hamulec'),
        help_text=_('Hamulec ręczny zaciągnięty'))
    tireblock = models.BooleanField(default=False, db_column='tireBlock',
        verbose_name=_('Blokada na koło'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vehicles:show', kwargs={'pk': self.pk})

    def check_permissions(self, user):
        """Czy dany użytkownik może przeglądać pojazd"""
        if user is None:
            return False

        # Sprawdź czy postać jest właścicielem pojazdu
        if self.ownertype == settings.RP_VEHICLE_OWNER_TYPE_ID_CHARACTER:
            if apps.get_model(app_label='characters',
                    model_name='Character').objects.filter(
                    pk=self.ownerid, memberid=user).count():
                return True

        # Sprwadź czy gracz należy do grupy, która jest właścicielem pojazdu
        if self.ownertype == settings.RP_VEHICLE_OWNER_TYPE_ID_GROUP:
            if apps.get_model(app_label='groups',
                    model_name='GroupMember').objects.filter(
                    userid__in=user.characters.all(),
                    groupid=self.ownerid).count():
                return True

        return False

    def get_owner(self):
        """Zwróć obiekt właściciela"""
        # Postać
        if self.ownertype == settings.RP_VEHICLE_OWNER_TYPE_ID_CHARACTER:
            try:
                return apps.get_model(app_label='characters',
                    model_name='Character').objects.get(pk=self.ownerid)
            except apps.get_model(app_label='characters',
                    model_name='Character').DoesNotExist:
                return None

        # Grupa
        if self.ownertype == settings.RP_VEHICLE_OWNER_TYPE_ID_GROUP:
            try:
                return apps.get_model(app_label='groups',
                    model_name='Group').objects.get(pk=self.ownerid)
            except apps.get_model(app_label='groups',
                    model_name='Group').DoesNotExist:
                return None

        return None

    class Meta:
        db_table = '_vehicles'
        verbose_name = _('pojazd')
        verbose_name_plural = _('pojazdy')
