from django.db import models
from django_unixdatetimefield import UnixDateTimeField
from jsonfield import JSONField
from django.utils.translation import ugettext as _

class Item(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=32, verbose_name=_('Nazwa przedmiotu'))
    OWNERTYPE_CHOICES = (
        (0, _('Na ziemi')),
        (1, _('Postać')),
        (3, _('Pojazd')),
        (4, _('Drzwi')),
    )
    ownertype = models.PositiveSmallIntegerField(db_column='ownerType',
        choices=OWNERTYPE_CHOICES, db_index=True)
    owner = models.IntegerField(db_index=True, verbose_name=_('ID właściciela'),
        blank=True, null=True)
    TYPE_CHOICES = (
        (1, _('Jakiś typ')),
    )
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES,
    verbose_name=_('Typ przedmiotu'))
    slotid = models.IntegerField(db_column='slotID', verbose_name=_('Numer '
        'slotu w ekwipunku'), blank=True, null=True)
    val1 = models.IntegerField(blank=True, null=True, verbose_name=_('Wartość '
        '1'))
    val2 = models.IntegerField(blank=True, null=True, verbose_name=_('Wartość '
        '2'))
    val3 = models.TextField(blank=True, null=True, verbose_name=_('Wartość '
        '3'))
    volume = models.IntegerField(blank=True, null=True,
        verbose_name=_('Objętość'))
    created = UnixDateTimeField(auto_now_add=True, verbose_name=_('Data '
        'stworzenia przedmiotu'))
    lastused = UnixDateTimeField(db_column='lastUsed', verbose_name=_('Ostatnio'
        ' użyty'), blank=True, null=True)
    lastuseddata = JSONField(db_column='lastUsedData', verbose_name=_('Odciski '
        'palców'), blank=True, null=True)
    used = models.BooleanField(default=False, verbose_name=_('W użytku'),
        help_text=_('Obecnie używany przez gracza'))
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    rx = models.FloatField(blank=True, null=True)
    ry = models.FloatField(blank=True, null=True)
    rz = models.FloatField(blank=True, null=True)
    interior = models.IntegerField(blank=True, null=True)
    dimension = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = '_items'

class Order(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    ordersize = models.IntegerField(db_column='orderSize', blank=True, null=True)
    catid = models.IntegerField(db_column='catID')
    data = JSONField()
    price = models.IntegerField()
    name = models.CharField(max_length=255)
    ordertype = models.IntegerField(db_column='orderType')

    class Meta:
        managed = False
        db_table = '_orders'


class OrderCategory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ordertype = models.IntegerField(db_column='orderType')  # Field name made lowercase.
    #orderowner = models.ForeignKey('groups.Group', db_column='orderOwner')
    orderowner = models.IntegerField(db_column='orderOwner')
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = '_ordersCat'

class Deposite(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    intid = models.IntegerField(db_column='intID')  # Field name made lowercase.
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    itemtype = models.IntegerField(db_column='itemType')  # Field name made lowercase.
    itemval1 = models.IntegerField(db_column='itemVal1')  # Field name made lowercase.
    itemval2 = models.IntegerField(db_column='itemVal2')  # Field name made lowercase.
    itemval3 = models.CharField(db_column='itemVal3', max_length=255)  # Field name made lowercase.
    itemvolume = models.IntegerField(db_column='itemVolume')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_deposite'

class Delivery(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    intid = models.IntegerField(db_column='intID')  # Field name made lowercase.
    pieces = models.IntegerField()
    data = JSONField()
    name = models.CharField(max_length=255)
    ordertype = models.IntegerField(db_column='orderType')  # Field name made lowercase.
    delivergroup = models.IntegerField(db_column='deliverGroup')  # ID grupy kuriera
    deliverid = models.IntegerField(db_column='deliverID')  # ID kuriera
    time = models.IntegerField()
    cost = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_delivers'
