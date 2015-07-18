from django import forms
from .models import GroupRank, GroupMember

class RankEditForm(forms.ModelForm):
    class Meta:
        model = GroupRank
        fields = ['name', 'cash', 'perms']

class MemberEditForm(forms.ModelForm):
    class Meta:
        model = GroupMember
        fields = ['rankid']
