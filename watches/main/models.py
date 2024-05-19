from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator

from watches.constants import (
    CONDITIONS_CHOICES, AVAILABILITY_CHOICES, SPECIALS_CHOICES,
    FOR_WHO_CHOICES, SHAPES_CHOICES, MATERIALS_CHOICES, MECHANISM_CHOICES,
    MIN_WATCH_PRICE
)


class Base(models.Model):

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Watch(Base):
    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Название часов',
        help_text=(
            'Уникальное, обязательное поле.'
        )
    )
    is_on_main = models.BooleanField(
        verbose_name='Выводить ли на главной?'
    )
    condition = models.ForeignKey(
        'ConditionChoice',
        max_length=255,
        on_delete=models.SET_DEFAULT,
        default=1,
        verbose_name='Состояние'
    )
    availability = models.ForeignKey(
        'AvailabilityChoice',
        max_length=255,
        on_delete=models.SET_DEFAULT,
        default=1,
        verbose_name='Наличие'
    )
    brand = models.ForeignKey(
        'Brand',
        on_delete=models.SET_DEFAULT,
        default=1,
        verbose_name='Бренд'
    )
    special = models.ForeignKey(
        'Special',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Спецпредложения'
    )
    for_who = models.ForeignKey(
        'ForWho',
        on_delete=models.SET_DEFAULT,
        default=1,
        verbose_name='Для кого'
    )
    shape = models.ForeignKey(
        'Shape',
        on_delete=models.SET_DEFAULT,
        default=1,
        verbose_name='Форма корпуса'
    )
    material = models.ForeignKey(
        'Material',
        on_delete=models.SET_DEFAULT,
        default=1,
        verbose_name='Категория материала корпуса',
        help_text='Для фильтра на странице со списком часов.'
    )
    material_alt = models.CharField(
        max_length=255,
        verbose_name='Материал корпуса',
        help_text=(
            'Для лучшего отображения на детальной странице часов. '
            'Обязательное поле.'
        )
    )
    price = models.PositiveIntegerField(
        validators=[
            MinValueValidator(
                MIN_WATCH_PRICE,
                message=f'Цена не может быть ниже {MIN_WATCH_PRICE}'
            )
        ],
        verbose_name='Цена часов'
    )
    type = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Тип',
        help_text=(
            'Например: "Классические". '
            'Необязательное поле.'
        )
    )
    waterproof = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Водонепроницаемость',
        help_text=(
            'Указывать в метрах. Например: "50 м". '
            'Необязательное поле.'
        )
    )
    diameter = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Диаметр корпуса',
        help_text=(
            'Указывать в миллиметрах. Например: "37 мм". '
            'Необязательное поле.'
        )
    )
    color = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Цвет циферблата',
        help_text=(
            'Необязательное поле.'
        )
    )
    bezel = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Безель',
        help_text=(
            'Внешнее поворотное кольцо вокруг циферблата часов. '
            'Необязательное поле.'
        )
    )
    glass = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Стекло',
        help_text=(
            'Необязательное поле.'
        )
    )
    reserve = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Запас хода',
        help_text=(
            'Необязательное поле.'
        )
    )
    caliber = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Калибр',
        help_text=(
            'Необязательное поле.'
        )
    )
    mechanism = models.CharField(
        max_length=255,
        choices=MECHANISM_CHOICES,
        null=True,
        blank=True,
        verbose_name='Механизм часов',
        help_text=(
            'Механические, автоматические и кварцевые. '
            'Необязательное поле.'
        )
    )
    functions = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Функции',
        help_text=(
            'Например: "Дата, часы, минуты, секунды". '
            'Необязательное поле.'
        )
    )
    strap = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Материал ремешка',
        help_text=(
            'Например: "Браслет из желтого золота 18к". '
            'Необязательное поле.'
        )
    )
    equipment = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Комплектация',
        help_text=(
            'Например: "Полный комплект" или "Коробка". '
            'Необязательное поле.'
        )
    )
    date_issue = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Дата выпуска',
        help_text=(
            'Необязательное поле.'
        )
    )
    reference = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Референсный номер',
        help_text=(
            'Уникальное, обязательное поле.'
        )
    )
    image = models.ImageField(
        default=None,
        null=True,
        blank=True,
        upload_to='watches_images',
        help_text=(
            'Необязательное поле, но очень желательное. '
            'Рекомендуемы размер: 400х400, формат: .webp'
        )
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Часы'
        verbose_name_plural = 'Часы'

    def get_absolute_url(self):
        return reverse(
            'main:watches_details', kwargs={'watch_id': self.pk}
        )


class ConditionChoice(Base):
    title = models.CharField(
        max_length=255,
        choices=CONDITIONS_CHOICES,
        unique=True,
        verbose_name='Состояние'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния'


class AvailabilityChoice(Base):
    title = models.CharField(
        max_length=255,
        choices=AVAILABILITY_CHOICES,
        unique=True,
        verbose_name='Наличие'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Наличие'
        verbose_name_plural = 'Наличие'


class Brand(Base):
    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Бренд'
    )

    class Meta:
        ordering = ['-title']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Special(Base):
    title = models.CharField(
        max_length=255,
        choices=SPECIALS_CHOICES,
        unique=True,
        verbose_name='Спецпредложения'
    )

    class Meta:
        ordering = ['-title']
        verbose_name = 'Спецпредложение'
        verbose_name_plural = 'Спецпредложения'


class ForWho(Base):
    title = models.CharField(
        max_length=255,
        choices=FOR_WHO_CHOICES,
        unique=True,
        verbose_name='Для кого'
    )

    class Meta:
        ordering = ['-title']
        verbose_name = 'Для кого'
        verbose_name_plural = 'Для кого'


class Shape(Base):
    title = models.CharField(
        max_length=255,
        choices=SHAPES_CHOICES,
        unique=True,
        verbose_name='Форма корпуса'
    )

    class Meta:
        ordering = ['-title']
        verbose_name = 'Форма корпуса'
        verbose_name_plural = 'Формы корпусов'


class Material(Base):
    title = models.CharField(
        max_length=255,
        choices=MATERIALS_CHOICES,
        unique=True,
        verbose_name='Материал корпуса'
    )

    class Meta:
        ordering = ['-title']
        verbose_name = 'Материал корпуса'
        verbose_name_plural = 'Материалы корпусов'
