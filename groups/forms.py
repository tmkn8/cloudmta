from django import forms
from django.utils.translation import ugettext as _
from django.db.models import Q
from django.apps import apps
from .models import GroupRank, GroupMember, GroupInvitation

class RankEditForm(forms.ModelForm):
    class Meta:
        model = GroupRank
        fields = ['name', 'cash', 'perms']

class MemberEditForm(forms.ModelForm):
    class Meta:
        model = GroupMember
        fields = ['rankid']

    def __init__(self, group_model, *args, **kwargs):
        super(MemberEditForm, self).__init__(*args, **kwargs)
        self.fields['rankid'].queryset = group_model.groupranks.all()

    def clean_rankid(self):
        rankid = self.cleaned_data.get('rankid')
        return rankid

class CreateGroupInvitationForm(forms.ModelForm):
    character = forms.CharField(label=_('Nazwa postaci'))

    class Meta:
        model = GroupInvitation
        fields = ['character']

    def clean_character(self):
        character_name = self.cleaned_data['character']
        character = None
        try:
            character = apps.get_model(app_label='characters',
                model_name='Character').objects.get(
                Q(name=character_name)
                |Q(facecode=character_name))
        except apps.get_model(app_label='characters',
                model_name='Character').DoesNotExist:
            raise forms.ValidationError(_('Podana postać nie istnieje.'))
        except apps.get_model(app_label='characters',
                model_name='Character').MultipleObjectsReturned:
            raise forms.ValidationError(_('Zwrócono kilka postaci. Spróbuj ponownie'))
        return character
