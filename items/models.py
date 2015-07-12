from django.db import models
from django_unixdatetimefield import UnixDateTimeField
from jsonfield import JSONField
from django.conf import settings
from django.utils.translation import ugettext as _

class Item(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True,
        verbose_name=_('ID przedmiotu'))
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
    type = models.PositiveSmallIntegerField(choices=settings.ITEM_TYPE_CHOICES,
    verbose_name=_('Typ przedmiotu'))
    slotid = models.IntegerField(db_column='slotID', verbose_name=_('Numer '
        'slotu w ekwipunku'), default=0)
    val1 = models.IntegerField(default=0, verbose_name=_('Wartość '
        '1'))
    val2 = models.IntegerField(default=0, verbose_name=_('Wartość '
        '2'))
    val3 = models.TextField(verbose_name=_('Wartość '
        '3'), blank=True, null=True)
    volume = models.IntegerField(default=0,
        verbose_name=_('Objętość'))
    created = UnixDateTimeField(auto_now_add=True, verbose_name=_('Data '
        'stworzenia przedmiotu'))
    lastused = UnixDateTimeField(db_column='lastUsed', verbose_name=_('Ostatnio'
        ' użyty'), blank=True, null=True)
    lastuseddata = JSONField(db_column='lastUsedData', verbose_name=_('Odciski '
        'palców'), blank=True, null=True)
    used = models.BooleanField(default=False, verbose_name=_('W użytku'),
        help_text=_('Obecnie używany przez gracza'))
    x = models.FloatField(default=0, verbose_name=_('Pozycja X'))
    y = models.FloatField(default=0, verbose_name=_('Pozycja Y'))
    z = models.FloatField(default=0, verbose_name=_('Pozycja Z'))
    # TODO: Trzeba zmienić verbose_name dla rx, ry, rz
    rx = models.FloatField(default=0, verbose_name=_('r X'))
    ry = models.FloatField(default=0, verbose_name=_('r Y'))
    rz = models.FloatField(default=0, verbose_name=_('r Z'))
    interior = models.IntegerField(default=0,
        verbose_name=_('Interior'))
    dimension = models.IntegerField(default=0,
        verbose_name=_('Wymiar'))

    class Meta:
        db_table = '_items'
        verbose_name = _('Przedmiot')
        verbose_name_plural = _('Przedmioty')

    def __str__(self):
        return self.name

class OrderType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Typ zamówień')
        verbose_name_plural = _('Typy zamówień')

class Order(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True,
        verbose_name='ID produktu')
    ordersize = models.IntegerField(db_column='orderSize',
        verbose_name=_('Rozmiar zamówienia'), help_text=_('W celu zapobiegania '
            'dostarczania dużych zamówień w małych pojazdach'))
    catid = models.ForeignKey('OrderCategory', related_name='category',
        db_column='catID')
    data = JSONField(blank=True, null=True)
    price = models.PositiveIntegerField(default=0, help_text=_('Pieniądze'),
        verbose_name=_('Cena produktu'))
    name = models.CharField(max_length=255, verbose_name=_('Nazwa produktu'))
    ordertype = models.ForeignKey('OrderType', db_column='orderType',
        verbose_name=_('Typ zamówienia'), related_name='orders',
        related_query_name='order')

    def __str__(self):
        return _("Zamówienie %d" % self.id)

    class Meta:
        db_table = '_orders'
        verbose_name = _('Produkt')
        verbose_name_plural = _('Produkty')


class OrderCategory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, verbose_name=_('ID '
        'kategorii'))
    name = models.CharField(max_length=255, verbose_name=_('Nazwa kategorii'))
    ordertype = models.ForeignKey('OrderType', db_column='orderType',
        verbose_name=_('Typ zamówienia'), related_name='ordercategories',
        related_query_name='ordercategory')
    # TODO: Dodaj realną relację modelu po dodaniu modelu grup
    # orderowner = models.ForeignKey('groups.Group', db_column='orderOwner',
    #    related_name='ordercategories', related_query_name='ordercategory')
    orderowner = models.IntegerField(db_column='orderOwner',
        verbose_name=_('Grupa'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = '_ordersCat'
        verbose_name = _('Kategoria produktów')
        verbose_name_plural = _('Kategorie produktów')

class Deposite(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, verbose_name=_('ID '
        'depozytu'))
    intid = models.IntegerField(db_column='intID', verbose_name=_('Drzwi'))
    # TODO: Dodaj realną relację modelu po dodaniu drzwi
    # intid = models.ForeignField(db_column='intID', verbose_name=_('Drzwi'),
    # related_name='deposites', related_query_name='deposite')
    name = models.CharField(max_length=255, verbose_name=_('Nazwa produktu'))
    stock = models.PositiveIntegerField(verbose_name=_('Ilość'), default=1)
    itemtype = models.IntegerField(db_column='itemType', verbose_name=_('Typ '
        'produktu'), choices=settings.ITEM_TYPE_CHOICES)
    itemval1 = models.IntegerField(db_column='itemVal1', default=0,
        verbose_name=_('Wartość produktu 1'))
    itemval2 = models.IntegerField(db_column='itemVal2', default=0,
        verbose_name=_('Wartość produktu 2'))
    itemval3 = models.TextField(db_column='itemVal3', null=True,
        blank=True, verbose_name=_('Wartość produktu 3'))
    itemvolume = models.IntegerField(db_column='itemVolume',
        verbose_name=_('Objętość produktu'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = '_deposite'
        verbose_name = _('Produkt w drzwiach')
        verbose_name_plural = _('Produkty w drzwiach')

class Delivery(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, verbose_name=_('ID '
        'dostarczenia'))
    intid = models.IntegerField(db_column='intID', verbose_name=_('Drzwi'),
        help_text=_('Do których dostaczany jest towar'))
    # TODO: Dodaj realną relację modelu po dodaniu drzwi
    # intid = models.ForeignField(db_column='intID', verbose_name=_('Drzwi'))
    pieces = models.IntegerField(default=1, verbose_name=_('Liczba sztuk'))
    data = JSONField(verbose_name=_('Informacje o produkcie'), blank=True,
        null=True)
    name = models.CharField(max_length=255, verbose_name=_('Nazwa zamówienia'))
    ordertype = models.ForeignKey('OrderType', db_column='orderType',
        verbose_name=_('Typ zamówienia'), related_name='deliveries',
        related_query_name='delivery')
    delivergroup = models.IntegerField(db_column='deliverGroup', default=0)
    # TODO: Dodaj relację do grup jak będzie już
    # delivergroup = models.ForeignKey('groups.Group', db_column='deliverGroup',
    # related_name='deliveries', related_query_name='delivery',
    # verbose_name=_('Grupa kurierska'))
    deliverid = models.ForeignKey('characters.Character',
        verbose_name=_('Dostawca'), related_name='deliveries',
        related_query_name='delivery')
    time = UnixDateTimeField(verbose_name='Czas', help_text=_('Odebranie paczki'
        ' przez kuriera'), blank=True, null=True)
    cost = models.PositiveIntegerField(verbose_name='Koszt', default=0,
        help_text=_('Pieniądze'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = '_delivers'
        verbose_name = _('Dostawa')
        verbose_name_plural = _('Dostawy')
