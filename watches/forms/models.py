from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

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


class Base(models.Model):
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    name = models.CharField(
        max_length=56,
        verbose_name='Имя клиента'
    )
    phone = PhoneNumberField()
    email = models.EmailField(
        max_length=255,
        verbose_name='Почта'
    )
    text = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return f'Клиент {self.name} оставил данные.'


class ShortMain(Base):
    pass


class Call(Base):
    pass


class Feedback(Base):
    tags = models.CharField(
        max_length=255,
        choices=TAGS_CHOICES
    )


class BuybackWatch(Base):

    communication_method = models.CharField(
        max_length=255,
        choices=COMMUNICATION_METHOD_CHOICES
    )
    brand = models.CharField(
        max_length=255,
    )
    model = models.CharField(
        max_length=255,
    )
    year = models.SmallIntegerField()
    price = models.IntegerField()
    condition = models.CharField(
        max_length=255,
        choices=CONDITIONS_FORM_CHOICES
    )
    equipment = models.CharField(
        max_length=255,
        choices=EQUIPMENT_FORM_CHOICES
    )
    images = models.FileField(
        upload_to='buyback_images'
    )


class WatchRequest(Base):
    hiden_info = models.TextField()
