from django.core.exceptions import ValidationError
from django.utils.timezone import now


def max_year_validator(value):
    current_year = now().year
    if value > current_year + 1:
        raise ValidationError(
            f'Значение года не может быть больше текущего: {current_year}'
        )
