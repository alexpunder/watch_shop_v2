from django import forms

from .models import ShortMain, Feedback, Call, WatchRequest


class ShortForm(forms.ModelForm):

    class Meta:
        model = ShortMain
        exclude = ('pub_date', 'email')
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Ваше имя'}
            ),
            'phone': forms.TextInput(
                attrs={'placeholder': 'Номер для связи'}
            ),
            # 'email': forms.TextInput(
            #     attrs={'placeholder': 'Электронная почта'}
            # ),
            'text': forms.TextInput(
                attrs={'placeholder': 'Сопроводительны текст'}
            )
        }


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        exclude = ('pub_date', 'email')


class CallForm(forms.ModelForm):

    class Meta:
        model = Call
        fields = ('name', 'phone', 'text')


class WatchRequestForm(forms.ModelForm):

    class Meta:
        model = WatchRequest
        exclude = ('pub_date', 'email')
