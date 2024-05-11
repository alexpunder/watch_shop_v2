from django.db import models

CONDITIONS_CHOICES = (
    ('Идеальное', 'Идеальное'),
    ('Как новые', 'Как новые'),
    ('Коллекционное состояние', 'Коллекционное состояние'),
    ('Новые', 'Новые'),  # TODO: поменять на "Абсолютно новые"
    ('Отличное', 'Отличное'),
    ('Хорошее', 'Хорошее'),
)

AVAILABILITY_CHOICES = (
    ('В наличии', 'В наличии'),
    ('Уточнить у менеджера', 'Уточнить у менеджера'),
)

SPECIALS_CHOICES = (
    ('Grand комплектация', 'Grand комплектация'),
    ('Limited editions', 'Limited editions'),
    ('Special editions', 'Special editions'),
    ('Акция', 'Акция'),
    ('Новинка', 'Новинка'),
    ('Тюнинг', 'Тюнинг'),
)

FOR_WHO_CHOICES = (
    ('Не задано', 'Не задано'),
    ('Мужские', 'Мужские'),
    ('Женские', 'Женские'),
    ('Унисекс', 'Унисекс'),
)

SHAPES_CHOICES = (
    ('Овальная', 'Овальная'),
    ('Круглая', 'Круглая'),
    ('Квадратная', 'Квадратная'),
    ('Бочка', 'Бочка'),
)

MATERIALS_CHOICES = (
    ('Желтое золото', 'Желтое золото'),
    ('Розовое золото', 'Розовое золото'),
    ('Белое золото', 'Белое золото'),
    ('Платина', 'Платина'),
    ('Титан', 'Титан'),
    ('Сталь', 'Сталь'),
    ('Карбон', 'Карбон'),
    ('Керамика', 'Керамика'),
    ('Прочие материалы', 'Прочие материалы'),
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
        verbose_name='Название часов'
    )
    is_on_main = models.BooleanField(
        verbose_name='Выводить ли на главной?'
    )
    condition = models.CharField(
        max_length=255,
        choices=CONDITIONS_CHOICES,
        verbose_name='Состояние'
    )
    availability = models.CharField(
        max_length=255,
        choices=AVAILABILITY_CHOICES,
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
        verbose_name='Материал корпуса'
    )
    price = models.PositiveSmallIntegerField(
        verbose_name='Цена часов'
    )
    type = models.CharField(
        max_length=255,
        verbose_name='Тип'
    )
    waterproof = models.CharField(
        max_length=255,
        verbose_name='Водонепроницаемость'
    )
    diameter = models.CharField(
        max_length=255,
        verbose_name='Диаметр корпуса'
    )
    color = models.CharField(
        max_length=255,
        verbose_name='Цвет циферблата'
    )
    bezel = models.CharField(
        max_length=255,
        verbose_name='Безель'
    )
    mechanism = models.CharField(
        max_length=255,
        verbose_name='Механизм часов'
    )
    functions = models.CharField(
        max_length=255,
        verbose_name='Функции'
    )
    strap = models.CharField(
        max_length=255,
        verbose_name='Материал ремешка'
    )
    equipment = models.CharField(
        max_length=255,
        verbose_name='Комплектация'
    )
    reference = models.CharField(
        max_length=255,
        verbose_name='Референсный номер'
    )
    image = models.ImageField(
        default=None,
        null=True,
        blank=True,
        upload_to='watches_images'
    )


class Brand(Base):
    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Бренд'
    )


class Special(Base):
    title = models.CharField(
        max_length=255,
        choices=SPECIALS_CHOICES,
        unique=True,
        verbose_name='Спецпредложения'
    )


class ForWho(Base):
    title = models.CharField(
        max_length=255,
        choices=FOR_WHO_CHOICES,
        unique=True,
        verbose_name='Для кого'
    )


class Shape(Base):
    title = models.CharField(
        max_length=255,
        choices=SHAPES_CHOICES,
        unique=True,
        verbose_name='Форма корпуса'
    )


class Material(Base):
    title = models.CharField(
        max_length=255,
        choices=MATERIALS_CHOICES,
        unique=True,
        verbose_name='Материал корпуса'
    )
