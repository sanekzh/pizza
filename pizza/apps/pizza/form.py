from __future__ import unicode_literals

from django import forms


class OrderForm(forms.Form):
    telephone = forms.RegexField(regex=r'^\d{9,15}$')
    email = forms.EmailField()
