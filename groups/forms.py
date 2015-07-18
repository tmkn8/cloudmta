from django import forms
from django.utils.translation import ugettext as _
from characters.models import Character
from .models import GroupRank, GroupMember, GroupInvitation

class RankEditForm(forms.ModelForm):
    class Meta:
        model = GroupRank
        fields = ['name', 'cash', 'perms']

class MemberEditForm(forms.ModelForm):
    class Meta:
        model = GroupMember
        fields = ['rankid']

class CreateGroupInvitationForm(forms.ModelForm):
    character = forms.CharField(label=_('Nazwa postaci'))

    class Meta:
        model = GroupInvitation
        fields = ['character']

    def clean_character(self):
        character_name = self.cleaned_data['character']
        character = None
        try:
            character = Character.objects.get(name=character_name)
        except Character.DoesNotExist:
            raise forms.ValidationError(_('Podana postać nie istnieje.'))
        except Character.MultipleObjectsReturned:
            raise forms.ValidationError(_('Zwrócono kilka postaci. Spróbuj ponownie'))
        return character
