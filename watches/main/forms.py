from django.core.exceptions import ValidationError
from django import forms

from forms.models import BuybackWatch
from watches.constants import MAX_IMAGES_FORM


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
        model = BuybackWatch
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
