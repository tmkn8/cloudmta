import datetime
from dateutil.relativedelta import relativedelta
from django import forms
from django.conf import settings
from django.utils.translation import ugettext as _
from .models import Character, StartSkin

class CreateCharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'sex', 'dob', 'skin']

    def clean_dob(self):
        """Sprawdź czy postać nie jest za młoda albo za stara"""
        dob = self.cleaned_data['dob']
        max_date_to_compare = datetime.date.today() - relativedelta(years=settings.RP_MIN_AGE_OF_CHARACTER)
        min_date_to_compare = datetime.date.today() - relativedelta(years=settings.RP_MAX_AGE_OF_CHARACTER)
        if dob > max_date_to_compare or dob < min_date_to_compare:
            raise forms.ValidationError(_("Twoja postać musi być urodzona "
            "pomiędzy %s oraz %s." % (min_date_to_compare, max_date_to_compare)))
        return dob

    def clean(self):
        """Sprawdź czy skin jest zgodny z płcią"""
        super(CreateCharacterForm, self).clean()
        skin = self.cleaned_data.get('skin', 0)
        sex = self.cleaned_data.get('sex', 0)
        if not StartSkin.objects.filter(skin_id=skin, sex=sex).count():
            raise forms.ValidationError(_('Wybrano nieprawidłowy skin. Spróbuj '
                'ponownie.'))

class CharacterSettingsForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['hide']
