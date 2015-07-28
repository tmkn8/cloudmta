from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from items.models import Item

class Door(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=60, verbose_name=_('nazwa'))
    OWNERTYPE_CHOICES = (
        (settings.RP_DOOR_OWNER_TYPE_ID_NONE, _('Brak')),
        (settings.RP_DOOR_OWNER_TYPE_ID_CHARACTER, _('Postać')),
        (settings.RP_DOOR_OWNER_TYPE_ID_GROUP, _('Grupa')),
    )
    ownertype = models.PositiveSmallIntegerField(db_column='ownerType',
        verbose_name=_('typ właściciela'), choices=OWNERTYPE_CHOICES,
        default=settings.RP_DOOR_OWNER_TYPE_ID_NONE)
    owner = models.PositiveIntegerField(verbose_name=_('ID właściciela'),
        default=0)
    dimension = models.PositiveIntegerField(verbose_name=_('wymiar'),
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
    locked = models.BooleanField(verbose_name=_('zamknięty'), help_text=_('czy '
        'pickup (drzwi) jest zamknięty'), default=True)

    def __str__(self):
        return _("Pickup drzwi %s" % self.parentid)

    class Meta:
        db_table = '_doorsPickup'
        verbose_name = _('pickup drzwi')
        verbose_name_plural = _('pickupy drzwi')

class Shop(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    shopid = models.ForeignKey('Door', db_column='shopID',
        verbose_name=_('drzwi sklepu'))
    price = models.PositiveIntegerField(verbose_name=_('Cena'))
    itemname = models.CharField(db_column='itemName', max_length=255,
        verbose_name=_('nazwa przedmiotu'))
    itemtype = models.PositiveSmallIntegerField(db_column='itemType',
        verbose_name=_('typ przedmiotu'), choices=Item.ITEM_TYPE_CHOICES)
    itemval1 = models.IntegerField(db_column='itemVal1', default=0,
        verbose_name=_('Wartość przedmiotu 1'))
    itemval2 = models.IntegerField(db_column='itemVal2', default=0,
        verbose_name=_('Wartość przedmiotu 2'))
    itemval3 = models.TextField(db_column='itemVal3', blank=True, null=True,
        verbose_name=_('Wartość przedmiotu 3'))
    itemvolume = models.IntegerField(db_column='itemVolume', default=0,
        verbose_name=_('Objętość przedmiotu'))

    def __str__(self):
        return _("%s w %s" % (self.itemname, self.shopid))

    class Meta:
        db_table = '_shops'
        verbose_name = _('produkt na /kup')
        verbose_name_plural = _('produkty na /kup')

class Clothes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    shopid = models.ForeignKey('Door', db_column='shopID',
        verbose_name=_('drzwi'))
    skinid = models.PositiveSmallIntegerField(db_column='skinID',
        verbose_name=_('ID skinu'), default=0)
    skinname = models.CharField(db_column='skinName', max_length=100,
        verbose_name=_('nazwa ubrania'))
    price = models.PositiveSmallIntegerField(default=0, verbose_name=_('cena'))

    def __str__(self):
        return _("Skin %d (%s) w %s" % (self.skinid, self.skinname,
            self.shopid))

    class Meta:
        db_table = '_clothes'
        verbose_name = _('skin na /ubrania')
        verbose_name = _('skiny na /ubrania')

class InteriorDetail(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name=_('nazwa'))
    x = models.FloatField(default=0, verbose_name=_('pozycja X'))
    y = models.FloatField(default=0, verbose_name=_('pozycja Y'))
    z = models.FloatField(default=0, verbose_name=_('pozycja Z'))
    a = models.FloatField(default=0, verbose_name=_('kąt'))
    int = models.PositiveIntegerField(default=0, verbose_name=_('wnętrze'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = '_intlist'
        verbose_name = _('dane interioru GTA')
        verbose_name_plural = _('dane interiorów GTA')

class Object(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    model = models.PositiveIntegerField(verbose_name=_('ID modelu'))
    x = models.FloatField(default=0, verbose_name=_('pozycja X'))
    y = models.FloatField(default=0, verbose_name=_('pozycja Y'))
    z = models.FloatField(default=0, verbose_name=_('pozycja Z'))
    rx = models.FloatField(default=0, verbose_name=_('rotacja X'))
    ry = models.FloatField(default=0, verbose_name=_('rotacja Y'))
    rz = models.FloatField(default=0, verbose_name=_('rotacja Z'))
    interior = models.PositiveIntegerField(default=0, verbose_name=_('wnętrze'))
    dimension = models.PositiveIntegerField(default=0, verbose_name=_('wymiar'))

    def __str__(self):
        return _("Obiekt %d" % self.id)

    class Meta:
        db_table = '_objects'
        verbose_name = _('obiekt')
        verbose_name_plural = _('obiekty')
