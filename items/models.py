from django.db import models
from django_unixdatetimefield import UnixDateTimeField
from jsonfield import JSONField
from django.conf import settings
from django.utils.translation import ugettext as _

class Item(models.Model):
    """Przedmioty"""
    id = models.AutoField(db_column='ID', primary_key=True,
        verbose_name=_('ID przedmiotu'))
    name = models.CharField(max_length=32, verbose_name=_('nazwa przedmiotu'))
    OWNERTYPE_CHOICES = (
        (settings.RP_ITEM_OWNER_TYPE_ID_NONE, _('na ziemi')),
        (settings.RP_ITEM_OWNER_TYPE_ID_CHARACTER, _('postać')),
        (settings.RP_ITEM_OWNER_TYPE_ID_VEHICLE, _('pojazd')),
        (settings.RP_ITEM_OWNER_TYPE_ID_DOOR, _('drzwi')),
    )
    ownertype = models.PositiveSmallIntegerField(db_column='ownerType',
        choices=OWNERTYPE_CHOICES, db_index=True)
    owner = models.IntegerField(db_index=True, verbose_name=_('ID właściciela'),
        blank=True, null=True)
    ITEM_TYPE_CHOICES = (
        (1, _('broń')),
        (2, _('amunicja')),
        (3, _('ubranie')),
        (4, _('megafon')),
        (5, _('kamizelka kuloodporna')),
        (6, _('jedzenie')),
        (7, _('ciało')),
        (8, _('telefon')),
        (9, _('rękawiczki')),
        (10, _('odznaka')),
        (11, _('identyfikator')),
        (12, _('płyta CD')),
        (13, _('narkotyki')),
        (14, _('paralizator')),
        (15, _('obiekt przyczepialny')),
        (16, _('maska')),
        (17, _('prawo jazdy')),
        (18, _('kajdanki')),
        (19, _('boombox')),
        (20, _('syrena policyjna')),
        (22, _('kostka do gry')),
    )
    type = models.PositiveSmallIntegerField(choices=ITEM_TYPE_CHOICES,
    verbose_name=_('typ przedmiotu'))
    slotid = models.IntegerField(db_column='slotID', verbose_name=_('numer '
        'slotu w ekwipunku'), default=0)
    val1 = models.IntegerField(default=0, verbose_name=_('wartość '
        '1'))
    val2 = models.IntegerField(default=0, verbose_name=_('wartość '
        '2'))
    val3 = models.TextField(verbose_name=_('wartość 3'), blank=True, null=True)
    volume = models.IntegerField(default=0, verbose_name=_('objętość'))
    created = UnixDateTimeField(auto_now_add=True, verbose_name=_('data '
        'stworzenia przedmiotu'))
    lastused = UnixDateTimeField(db_column='lastUsed', verbose_name=_('ostatnio'
        ' użyty'), blank=True, null=True)
    lastuseddata = JSONField(db_column='lastUsedData', verbose_name=_('odciski '
        'palców'), blank=True, null=True)
    used = models.BooleanField(default=False, verbose_name=_('w użytku'),
        help_text=_('obecnie używany przez gracza'))
    x = models.FloatField(default=0, verbose_name=_('pozycja X'))
    y = models.FloatField(default=0, verbose_name=_('pozycja Y'))
    z = models.FloatField(default=0, verbose_name=_('pozycja Z'))
    rx = models.FloatField(default=0, verbose_name=_('rotacja X'))
    ry = models.FloatField(default=0, verbose_name=_('rotacja Y'))
    rz = models.FloatField(default=0, verbose_name=_('rotacja Z'))
    interior = models.IntegerField(default=0,
        verbose_name=_('wnętrze'))
    dimension = models.IntegerField(default=0,
        verbose_name=_('wymiar'))

    class Meta:
        db_table = '_items'
        verbose_name = _('przedmiot')
        verbose_name_plural = _('przedmioty')

    def __str__(self):
        return self.name

class OrderType(models.Model):
    """Typ produktów na magazynie, np. LSPD"""
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('typ zamówień')
        verbose_name_plural = _('typy zamówień')

class Order(models.Model):
    """Produkty na magazynie"""
    id = models.AutoField(db_column='ID', primary_key=True,
        verbose_name='ID produktu')
    ordersize = models.IntegerField(db_column='orderSize',
        verbose_name=_('rozmiar zamówienia'), help_text=_('w celu zapobiegania '
            'dostarczania dużych zamówień w małych pojazdach'))
    catid = models.ForeignKey('OrderCategory', related_name='category',
        db_column='catID')
    data = JSONField(blank=True, null=True)
    price = models.PositiveIntegerField(default=0, help_text=_('pieniądze'),
        verbose_name=_('cena produktu'))
    name = models.CharField(max_length=255, verbose_name=_('nazwa produktu'))
    ordertype = models.ForeignKey('OrderType', db_column='orderType',
        verbose_name=_('typ zamówienia'), related_name='orders',
        related_query_name='order')

    def __str__(self):
        return _("Zamówienie %d" % self.id)

    class Meta:
        db_table = '_orders'
        verbose_name = _('produkt')
        verbose_name_plural = _('produkty')


class OrderCategory(models.Model):
    """Kategoria produktów na magazynie"""
    id = models.AutoField(db_column='ID', primary_key=True, verbose_name=_('ID '
        'kategorii'))
    name = models.CharField(max_length=255, verbose_name=_('nazwa kategorii'))
    ordertype = models.ForeignKey('OrderType', db_column='orderType',
        verbose_name=_('typ zamówienia'), related_name='ordercategories',
        related_query_name='ordercategory')
    orderowner = models.ForeignKey('groups.Group', db_column='orderOwner',
        related_name='ordercategories', related_query_name='ordercategory',
        verbose_name=_('grupa'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = '_ordersCat'
        verbose_name = _('kategoria produktów')
        verbose_name_plural = _('kategorie produktów')

class Deposite(models.Model):
    """Produkty w drzwiach"""
    id = models.AutoField(db_column='ID', primary_key=True, verbose_name=_('ID '
        'depozytu'))
    intid = models.ForeignKey('doors.Door', db_column='intID',
        verbose_name=_('drzwi'), related_name='deposites',
        related_query_name='deposite')
    name = models.CharField(max_length=255, verbose_name=_('nazwa produktu'))
    stock = models.PositiveIntegerField(verbose_name=_('ilość'), default=1)
    itemtype = models.IntegerField(db_column='itemType', verbose_name=_('Typ '
        'produktu'), choices=Item.ITEM_TYPE_CHOICES)
    itemval1 = models.IntegerField(db_column='itemVal1', default=0,
        verbose_name=_('wartość produktu 1'))
    itemval2 = models.IntegerField(db_column='itemVal2', default=0,
        verbose_name=_('wartość produktu 2'))
    itemval3 = models.TextField(db_column='itemVal3', null=True, blank=True,
        verbose_name=_('wartość produktu 3'))
    itemvolume = models.IntegerField(db_column='itemVolume', default=0,
        verbose_name=_('objętość produktu'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = '_deposite'
        verbose_name = _('produkt w drzwiach')
        verbose_name_plural = _('produkty w drzwiach')

class Delivery(models.Model):
    """Dostawy w trakcie"""
    id = models.AutoField(db_column='ID', primary_key=True, verbose_name=_('ID '
        'dostarczenia'))
    intid = models.ForeignKey('doors.Door', db_column='intID', verbose_name=_(
        'drzwi'), help_text=_('do których dostaczany jest towar'))
    pieces = models.IntegerField(default=1, verbose_name=_('liczba sztuk'))
    data = JSONField(verbose_name=_('informacje o produkcie'), blank=True,
        null=True)
    name = models.CharField(max_length=255, verbose_name=_('nazwa zamówienia'))
    ordertype = models.ForeignKey('OrderType', db_column='orderType',
        verbose_name=_('typ zamówienia'), related_name='deliveries',
        related_query_name='delivery')
    delivergroup = models.IntegerField(db_column='deliverGroup', default=0)
    delivergroup = models.ForeignKey('groups.Group', db_column='deliverGroup',
        related_name='deliveries', related_query_name='delivery',
        verbose_name=_('grupa kurierska'))
    deliverid = models.ForeignKey('characters.Character',
        verbose_name=_('dostawca'), related_name='deliveries',
        related_query_name='delivery')
    time = UnixDateTimeField(verbose_name='czas', help_text=_('odebranie paczki'
        ' przez kuriera'), blank=True, null=True)
    cost = models.PositiveIntegerField(verbose_name='koszt', default=0,
        help_text=_('pieniądze'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = '_delivers'
        verbose_name = _('dostawa')
        verbose_name_plural = _('dostawy')

class PhoneContact(models.Model):
    """Kontakty telefoniczne"""
    id = models.AutoField(db_column='ID', primary_key=True)
    phoneid = models.PositiveIntegerField(db_column='phoneID',
        verbose_name=_('ID telefonu'))
    number = models.PositiveIntegerField(verbose_name=_('numer kontaktu'))
    name = models.CharField(max_length=100, verbose_name=_('nazwa kontaktu'))

    def __str__(self):
        return _("Kontakt %s w telefonie o ID %d" % (self.name, self.phoneid))

    class Meta:
        db_table = '_phone_contacts'
        verbose_name = _('kontakt telefoniczny')
        verbose_name_plural = _('kontakty telefoniczne')
