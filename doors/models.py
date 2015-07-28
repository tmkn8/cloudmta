from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

class Door(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=60, verbose_name=_('Nazwa'))
    OWNERTYPE_CHOICES = (
        (settings.RP_DOOR_OWNER_TYPE_ID_NONE, _('Brak')),
        (settings.RP_DOOR_OWNER_TYPE_ID_CHARACTER, _('Postać')),
        (settings.RP_DOOR_OWNER_TYPE_ID_GROUP, _('Grupa')),
    )
    ownertype = models.PositiveSmallIntegerField(db_column='ownerType',
        verbose_name=_('Typ właściciela'), choices=OWNERTYPE_CHOICES,
        default=settings.RP_DOOR_OWNER_TYPE_ID_NONE)
    owner = models.PositiveIntegerField(verbose_name=_('ID właściciela'),
        default=0)
    dimension = models.PositiveIntegerField(verbose_name=_('Wymiar'),
        default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = '_doors'
        verbose_name = _('drzwi')
        verbose_name_plural = _('drzwi')

class DoorPickup(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    parentid = models.ForeignKey('Door', db_column='parentID',
        verbose_name=_('drzwi'))
    name = models.CharField(max_length=255, verbose_name=_('nazwa'))
    inx = models.FloatField(db_column='inX', verbose_name=_('pozycja wejścia '
        'X'), default=0)
    iny = models.FloatField(db_column='inY', verbose_name=_('pozycja wejścia '
        'Y'), default=0)
    inz = models.FloatField(db_column='inZ', verbose_name=_('pozycja wejścia '
        'Z'), default=0)
    outx = models.FloatField(db_column='outX', verbose_name=_('pozycja wyjścia '
        'X'), default=0)
    outy = models.FloatField(db_column='outY', verbose_name=_('pozycja wyjścia '
        'Y'), default=0)
    outz = models.FloatField(db_column='outZ', verbose_name=_('pozycja wyjścia '
        'Z'), default=0)
    indim = models.PositiveIntegerField(db_column='inDim',
        verbose_name=_('wymiar wejścia'), default=0)
    outdim = models.PositiveIntegerField(db_column='outDim',
        verbose_name=_('wymiar wyjścia'), default=0)
    inint = models.PositiveIntegerField(db_column='inInt',
        verbose_name=_('wnętrze wejścia'), default=0)
    outint = models.PositiveIntegerField(db_column='outInt',
        verbose_name=_('wnętrze wyjścia'), default=0)
    outmodel = models.PositiveIntegerField(db_column='outModel',
        verbose_name=_('model wyjścia'), default=0)
    inmodel = models.PositiveIntegerField(db_column='inModel',
        verbose_name=_('model wejścia'), default=0)
    inangle = models.FloatField(db_column='inAngle',
        verbose_name=_('kąt wejścia'), default=0)
    outangle = models.FloatField(db_column='outAngle', verbose_name=_('kąt '
        'wyjścia'), default=0)
    locked = models.BooleanField(verbose_name=_('Zamknięty'), help_text=_('Czy '
        'pickup jest zamknięty?'), default=True)

    def __str__(self):
        return _("Pickup drzwi %s" % self.parentid)

    class Meta:
        db_table = '_doorsPickup'
        verbose_name = _('pickup drzwi')
        verbose_name_plural = _('pickupy drzwi')
