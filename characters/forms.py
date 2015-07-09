from django import forms

class CreateCharacterForm(forms.ModelForm):
    class Meta:
        model = characters
        fields = ['lastname', 'sex', 'dob', 'skin']
