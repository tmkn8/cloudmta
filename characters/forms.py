import datetime
from dateutil.relativedelta import relativedelta
from django import forms
from django.conf import settings
from django.utils.translation import ugettext as _
from .models import Character

class CreateCharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'sex', 'dob', 'skin']

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        max_date_to_compare = datetime.date.today() - relativedelta(years=settings.RP_MIN_AGE_OF_CHARACTER)
        min_date_to_compare = datetime.date.today() - relativedelta(years=settings.RP_MAX_AGE_OF_CHARACTER)
        if dob > max_date_to_compare or dob < min_date_to_compare:
            raise forms.ValidationError(_("Twoja postać musi być urodzona "
            "pomiędzy %s oraz %s." % (min_date_to_compare, max_date_to_compare)))
        return dob

    def clean(self):
        super(CreateCharacterForm, self).clean()
        # TODO: Validate if skin matches sex
