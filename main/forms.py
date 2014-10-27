from ibus.keysyms import value
from django import forms


class RateForm(forms.Form):
    value = forms.IntegerField(label='Value')
    comment = forms.CharField(label='Comment',max_length=500)