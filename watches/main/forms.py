from django import forms

from forms.models import BuybackWatch


class ExtendBuybackForm(forms.ModelForm):

    class Meta:
        model = BuybackWatch
        exclude = ('pub_date', 'text')
