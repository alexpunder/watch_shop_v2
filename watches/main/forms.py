from django import forms
from phonenumber_field.formfields import PhoneNumberField

TAGS_CHOICES = (
    ('Общий вопрос', 'Общий вопрос'),
    ('Пожелания', 'Пожелания'),
    ('Обнаружена ошибка', 'Обнаружена ошибка'),
)

COMMUNICATION_METHOD_CHOICES = (
    ('Звонок', 'Звонок'),
    ('На почту', 'На почту'),
    ('Telegram', 'Telegram'),
    ('WhatsUp', 'WhatsUp'),
    ('Viber', 'Viber'),
)

CONDITIONS_FORM_CHOICES = (
    ('Идеальное', 'Идеальное'),
    ('Новое', 'Новое'),
    ('Естественные следы носки', 'Естественные следы носки'),
    ('Есть дефекты', 'Есть дефекты'),
    ('Требуется ремонт', 'Требуется ремонт'),
)

EQUIPMENT_FORM_CHOICES = (
    ('С упаковкой', 'С упаковкой'),
    ('Без упаковки', 'Без упаковки'),
)


class ShortMainForm(forms.Form):
    name = forms.CharField(
        max_length=56,
        widget=forms.TextInput(attrs={'placeholder': 'Имя'})
    )
    phone = PhoneNumberField(
        widget=forms.TextInput(attrs={'placeholder': 'Номер для связи'})
    )


class ShortFeedbackForm(ShortMainForm):
    tag = forms.ChoiceField(
        choices=TAGS_CHOICES
    )
    text = forms.CharField(
        max_length=255,
        widget=forms.Textarea(attrs={'placeholder': 'Текст сообщения'})
    )


class ExtendBuybackForm(ShortMainForm):
    communication_method = forms.ChoiceField(
        choices=COMMUNICATION_METHOD_CHOICES
    )
    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(attrs={'placeholder': 'Почта'})
    )
    brand = forms.CharField(
        max_length=255,
    )
    model = forms.CharField(
        max_length=255,
    )
    year = forms.IntegerField()
    price = forms.IntegerField()
    condition = forms.ChoiceField(
        choices=CONDITIONS_FORM_CHOICES
    )
    equipment = forms.ChoiceField(
        choices=EQUIPMENT_FORM_CHOICES
    )
    images = forms.FileField(
        # widget=forms.FileInput(attrs={
        #     'multiple': True,
        # })
    )
