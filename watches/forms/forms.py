from django import forms
from django.core.exceptions import ValidationError
from django import forms

from watches.constants import MAX_IMAGES_FORM
from .models import (
    ShortMain, Feedback, Call, WatchRequest,
    BuybackWatches, ValuationWatches
)


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
        exclude = ('pub_date',)

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
        exclude = ('pub_date',)

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
        exclude = ('pub_date', 'email')
        # widgets = {
        #     'name': forms.TextInput(
        #         attrs={'placeholder': 'Ваше имя'}
        #     ),
        #     'phone': forms.TextInput(
        #         attrs={'placeholder': 'Номер для связи'}
        #     ),
        #     'text': forms.TextInput(
        #         attrs={'placeholder': 'Сопроводительны текст'}
        #     )
        # }


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        exclude = ('pub_date',)


class CallForm(forms.ModelForm):

    class Meta:
        model = Call
        exclude = ('pub_date',)


class WatchRequestForm(forms.ModelForm):

    class Meta:
        model = WatchRequest
        exclude = ('pub_date',)
