from django.db import models
from django.utils.translation import ugettext as _
from jsonfield import JSONField

class Group(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True,
        verbose_name=_('ID grupy'))
    members = models.ManyToManyField('characters.Character',
        through='GroupMember', through_fields=('groupid', 'userid'),
        related_name='groups', related_query_name='group')
    name = models.CharField(max_length=64, verbose_name=_('Nazwa'))
    tag = models.CharField(max_length=4, verbose_name=_('Tag'))
    r = models.PositiveSmallIntegerField(verbose_name=_('Kolor R'), default=0)
    g = models.PositiveSmallIntegerField(verbose_name=_('Kolor G'), default=0)
    b = models.PositiveSmallIntegerField(verbose_name=_('Kolor B'), default=0)
    ordertype = models.ForeignKey('items.OrderType', db_column='orderType',
        verbose_name=_('Typ zamówienia'), null=True, blank=True)
    perms = JSONField(blank=True, null=True, verbose_name=_('Uprawnienia grupy'))
    cash = models.PositiveIntegerField(default=0, verbose_name=_('Pieniądze grupy'))

    def get_group_permissions(self):
        """Pobierz listę uprawnień grupy jako listę"""
        try:
            perms = self.perms[0]
        except ValueError:
            return None
        except KeyError:
            return None

        # Przekształć uprawnienia grupy w listę
        group_permissions = []
        for perm in perms:
            if perms[perm]:
                group_permissions.append(perm)

        return group_permissions

    def can_user_access_group(self, user):
        """Sprawdź czy użytkownik może odwiedzać panel tej grupy"""
        if GroupMember.objects.filter(userid__in=user.characters.all(),
                groupid=self).count():
            return True
        return False

    def get_user_permissions(self, user):
        """Pobierz listę uprawnień grupowych danego użytkownika"""
        user_perms = {}

        # Pobierz członkostwa danego użytkownika w tej grupie
        members = self.groupmembers.filter(userid__in=user.characters.all())
        # Zwróć null, jeżeli użytkownik nie ma żadnych członkostw w grupie
        if not members:
            return None

        # Iteruj przez wszystkie członkostwa użytkownika
        for member in members:
            # Pobierz uprawnienia dla rangi danego członkostwa
            rank_perms = member.rankid.get_rank_permissions()
            # Zwróć null, jeżeli ranga nie posiada uprawnień
            if not rank_perms:
                return None

            # Iteruj przez uprawnienia rangi
            for key in rank_perms:
                # Jeżeli uprawnienie rangi jest true, wtedy
                # je ustaw użytkownikowi na tą samą wartość
                try:
                    if rank_perms[key]:
                        user_perms[key] = rank_perms[key]

                    # Jeżeli wartość jest jeszcze nieustawiona, wywołaj wyjątek
                    # i ustaw w nim false
                    user_perms[key]
                except KeyError:
                    user_perms[key] = False

        return user_perms

    class Meta:
        db_table = '_groups'
        verbose_name = _('grupa')
        verbose_name_plural = _('grupy')

    def __str__(self):
        return self.name

class GroupMember(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    userid = models.ForeignKey('characters.Character', db_column='userID',
        verbose_name=_('Postać'), related_name=_('groupmembers'),
        related_query_name=_('groupmember'))
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

    def get_rank_permissions(self):
        """Pobierz uprawnienia rangi z JSON do dicitonary

        Waliduje z listą uprawnień grupy. Nie przepuści wartości spoza uprawnień grupy."""
        try:
            if self.perms:
                perms = self.perms[0]
            else:
                perms = {}
        except ValueError:
            return None
        except KeyError:
            return None

        # Pobierz uprawnienia grupy
        group_perms = self.groupid.get_group_permissions()

        # Wyzeruj wszystkie uprawnienia rangi
        rank_perms = {}
        for key in group_perms:
            rank_perms[key] = False

        # Iteruj przez uprawnienia grupy i przypisz uprawnienia rangi
        for key in group_perms:
            try:
                rank_perms[key] = perms[key]
            except KeyError:
                rank_perms[key] = False

        return rank_perms
