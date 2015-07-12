from django.db import models
from django.utils.translation import ugettext as _
from jsonfield import JSONField

class Group(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True,
        verbose_name=_('ID grupy'))
    name = models.CharField(max_length=64, verbose_name=_('Nazwa'))
    tag = models.CharField(max_length=4, verbose_name=_('Tag'))
    r = models.PositiveSmallIntegerField(verbose_name=_('Kolor R'), default=0)
    g = models.PositiveSmallIntegerField(verbose_name=_('Kolor G'), default=0)
    b = models.PositiveSmallIntegerField(verbose_name=_('Kolor B'), default=0)
    ordertype = models.ForeignKey('items.OrderType', db_column='orderType',
        verbose_name=_('Typ zamówienia'), null=True, blank=True)
    perms = JSONField(blank=True, null=True, verbose_name=_('Uprawnienia grupy'))
    cash = models.PositiveIntegerField(default=0, verbose_name=_('Pieniądze grupy'))

    class Meta:
        db_table = '_groups'
        verbose_name = _('grupa')
        verbose_name_plural = _('grupy')

    def __str__(self):
        return self.name

class GroupMember(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    userid = models.ForeignKey('characters.Character', db_column='userID',
        verbose_name=_('Postać'), related_name=_('characters'),
        related_query_name=_('character'))
    rankid = models.ForeignKey('GroupRank', db_column='rankID',
        verbose_name=_('Ranga'), related_name='groupsmembers',
        related_query_name='groupmembers')
    groupid = models.ForeignKey('Group', db_column='groupID',
        verbose_name=_('Grupa'), related_name='groupmembers',
        related_query_name='groupmember')

    class Meta:
        db_table = '_groups_members'
        verbose_name = _('członek')
        verbose_name_plural = _('członkowie')

    def __str__(self):
        return _("%s w %s" % (self.userid, self.groupid))

class GroupRank(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=64, verbose_name=_('Nazwa'),
        default=_('Ranga'))
    groupid = models.ForeignKey('Group', db_column='groupID',
        related_name='groupranks', related_query_name='grouprank',
        verbose_name=_('Grupa'))
    cash = models.PositiveIntegerField(verbose_name=_('Wypłata'), default=0)
    defaultrank = models.BooleanField(db_column='defaultRank', default=False,
        verbose_name=_('Domyślna ranga'), help_text=_('Ranga, na którą '
        'trafiają nowi gracze. Musi być chociaż jedna w grupie.'))
    perms = JSONField(verbose_name=_('Uprawnienia'), blank=True, null=True)

    class Meta:
        db_table = '_groups_ranks'
        verbose_name = _('ranga')
        verbose_name_plural = _('rangi')

    def __str__(self):
        return self.name
