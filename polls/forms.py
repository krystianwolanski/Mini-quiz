from django import forms

class NameForm(forms.Form):
    Odp = forms.ChoiceField(label='Odp')