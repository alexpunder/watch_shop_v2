from django import forms
from django.core.exceptions import ValidationError

from watches.constants import MAX_IMAGES_FORM

from .models import (BuybackWatches, Call, Feedback, ShortMain,
                     ValuationWatches, WatchRequest)


class ExtendValuationForm(forms.ModelForm):
    valuation_images = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                'name': 'valuation_images',
                'id': 'valuation_images',
                'multiple': True,
                'class': 'custom-file-input'
            }
        )
    )

    class Meta:
        model = ValuationWatches
        exclude = ('pub_date', 'processed')

    def clean(self):
        cleaned_data = super().clean()
        images = self.files.getlist('valuation_images')
        if len(images) > MAX_IMAGES_FORM:
            raise ValidationError(
                f'Можно загрузить максимум {MAX_IMAGES_FORM}.'
            )
        elif len(images) < 1:
            raise ValidationError(
                'Необходимо загрузите хотя бы одно изображение'
            )
        return cleaned_data


class ExtendBuybackForm(forms.ModelForm):
    buyback_images = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                'name': 'buyback_images',
                'id': 'buyback_images',
                'multiple': True,
                'class': 'custom-file-input'
            }
        )
    )

    class Meta:
        model = BuybackWatches
        exclude = ('pub_date', 'processed')

    def clean(self):
        cleaned_data = super().clean()
        images = self.files.getlist('buyback_images')
        if len(images) > MAX_IMAGES_FORM:
            raise ValidationError(
                f'Можно загрузить максимум {MAX_IMAGES_FORM}.'
            )
        elif len(images) < 1:
            raise ValidationError(
                'Необходимо загрузите хотя бы одно изображение'
            )
        return cleaned_data


class ShortForm(forms.ModelForm):

    class Meta:
        model = ShortMain
        exclude = ('pub_date', 'processed')


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        exclude = ('pub_date', 'processed')


class CallForm(forms.ModelForm):

    class Meta:
        model = Call
        exclude = ('pub_date', 'processed')


class WatchRequestForm(forms.ModelForm):

    class Meta:
        model = WatchRequest
        exclude = ('pub_date', 'processed')
