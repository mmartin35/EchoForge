from  django import forms

class DirectionForm(forms.Form):
    direction = forms.IntegerField(required=True)

class ResetForm(forms.Form):
    is_reset = forms.BooleanField(required=True)
