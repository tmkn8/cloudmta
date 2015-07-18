from django import forms
from .models import GroupRank

class RankEditForm(forms.ModelForm):
    class Meta:
        model = GroupRank
        fields = ['name', 'cash', 'perms']
