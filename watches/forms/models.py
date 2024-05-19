from django.db import models
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

from .validations import max_year_validator
from watches.constants import (
    TAGS_CHOICES, COMMUNICATION_METHOD_CHOICES, CONDITIONS_FORM_CHOICES,
    EQUIPMENT_FORM_CHOICES, DT_FORMAT, MIN_YEAR_BUYBACK, MIN_PRICE_BUYBACK
)


class Base(models.Model):
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата обращения'
    )
    processed = models.BooleanField(
        default=False,
        verbose_name='Обработан?'
    )
    name = models.CharField(
        max_length=56,
        verbose_name='Имя клиента'
    )
    phone = PhoneNumberField(
        verbose_name='Номер телефона'
    )
    text = models.TextField(
        blank=True,
        null=True,
        verbose_name='Текст сообщения',
    )

    class Meta:
        abstract = True
        ordering = ['-pub_date']


class ShortMain(Base):

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Малая форма'
        verbose_name_plural = 'Малая форма'

    def __str__(self):
        return (
            f'Клиент {self.name} оставил обращение от '
            f'{self.pub_date.strftime(DT_FORMAT)}'
        )


class Call(Base):

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Заказ звонка'
        verbose_name_plural = 'Заказы звонков'

    def __str__(self):
        return (
            f'Клиент {self.name} заказал звонок от '
            f'{self.pub_date.strftime(DT_FORMAT)}'
        )


class Feedback(Base):
    tags = models.CharField(
        max_length=255,
        choices=TAGS_CHOICES,
        verbose_name='Категория обращения'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return (
            f'Клиент {self.name} оставил обратную связь от '
            f'{self.pub_date.strftime(DT_FORMAT)}'
        )


class BuybackWatches(Base):
    email = models.EmailField(
        max_length=255,
        verbose_name='Почта'
    )
    communication_method = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        choices=COMMUNICATION_METHOD_CHOICES,
        verbose_name='Предпочитаемый способ связи'
    )
    brand = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Бренд'
    )
    model = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Модель'
    )
    year = models.SmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(
                MIN_YEAR_BUYBACK,
                message=(
                    f'Значение года не может быть меньше {MIN_YEAR_BUYBACK}г.'
                )
            ),
            max_year_validator
        ],
        verbose_name='Год покупки'
    )
    price = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(
                MIN_PRICE_BUYBACK,
                message=f'Значение не может быть меньше {MIN_PRICE_BUYBACK}.'
            )
        ],
        verbose_name='Желаемая сумма (руб.)'
    )
    condition = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        choices=CONDITIONS_FORM_CHOICES,
        verbose_name='Состояние часов'
    )
    equipment = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        choices=EQUIPMENT_FORM_CHOICES,
        verbose_name='Комплектация'
    )

    class Meta:
        verbose_name = 'Выкуп часов'
        verbose_name_plural = 'Выкуп часов'

    def __str__(self):
        return (
            f'Клиент {self.name} оставил запрос на выкуп от '
            f'{self.pub_date.strftime(DT_FORMAT)}'
        )


class BuybackImage(models.Model):
    buyback = models.ForeignKey(
        'BuybackWatches',
        related_name='images',
        on_delete=models.SET_NULL,
        null=True
    )
    image = models.ImageField(
        upload_to='buyback_images',
        verbose_name='Изображения часов из заявки на выкуп'
    )

    class Meta:
        verbose_name = 'Изображение из заявки'
        verbose_name_plural = 'Изображения из заявки'

    def __str__(self):
        return f'Изображение часов #{self.id}'


class ValuationWatches(Base):
    email = models.EmailField(
        max_length=255,
        verbose_name='Почта'
    )
    communication_method = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        choices=COMMUNICATION_METHOD_CHOICES,
        verbose_name='Предпочитаемый способ связи'
    )
    brand = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Бренд'
    )
    model = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Модель'
    )
    year = models.SmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(
                MIN_YEAR_BUYBACK,
                message=(
                    f'Значение года не может быть меньше {MIN_YEAR_BUYBACK}г.'
                )
            ),
            max_year_validator
        ],
        verbose_name='Год покупки'
    )
    price = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(
                MIN_PRICE_BUYBACK,
                message=f'Значение не может быть меньше {MIN_PRICE_BUYBACK}.'
            )
        ],
        verbose_name='Желаемая сумма (руб.)'
    )
    condition = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        choices=CONDITIONS_FORM_CHOICES,
        verbose_name='Состояние часов'
    )
    equipment = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        choices=EQUIPMENT_FORM_CHOICES,
        verbose_name='Комплектация'
    )

    class Meta:
        verbose_name = 'Оценка часов'
        verbose_name_plural = 'Оценка часов'

    def __str__(self):
        return (
            f'Клиент {self.name} оставил запрос на оценку от '
            f'{self.pub_date.strftime(DT_FORMAT)}'
        )


class ValuationImage(models.Model):
    valuation = models.ForeignKey(
        'ValuationWatches',
        related_name='val_images',
        on_delete=models.SET_NULL,
        null=True
    )
    image = models.ImageField(
        upload_to='valuation_images',
        verbose_name='Изображения часов из заявки на оценку'
    )

    class Meta:
        verbose_name = 'Изображение из заявки на оценку'
        verbose_name_plural = 'Изображения из заявок на оценку'

    def __str__(self):
        return f'Изображение часов #{self.id}'


class WatchRequest(Base):
    hiden_info = models.TextField(
        verbose_name='Данные запрашиваемых часов',
        help_text=(
            'id: уникальный идентификатор часов; '
            'ref: уникальный референсный номер.'
        )
    )

    class Meta:
        verbose_name = 'Запрос на часы'
        verbose_name_plural = 'Запросы на часы'

    def __str__(self):
        return (
            f'Клиент {self.name} оставил запрос на часы от '
            f'{self.pub_date.strftime(DT_FORMAT)}'
        )
