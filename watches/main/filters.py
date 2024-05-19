import django_filters
from django import forms
from django.db.models import Q


from .models import (
    Watch, ConditionChoice, AvailabilityChoice, Brand, Special,
    ForWho, Shape, Material
)


class SearchFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_by_multiple_fields')

    class Meta:
        model = Watch
        fields = ('search',)

    def filter_by_multiple_fields(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value)
            | Q(condition__title__icontains=value)
            | Q(brand__title__icontains=value)
            | Q(for_who__title__icontains=value)
            | Q(shape__title__icontains=value)
            | Q(material__title__icontains=value)
            | Q(color__icontains=value)
            | Q(reference__icontains=value)
        )


class WatchesFilter(django_filters.FilterSet):
    condition = django_filters.ModelChoiceFilter(
        queryset=ConditionChoice.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label='',
        empty_label='Состояние'
    )
    availability = django_filters.ModelChoiceFilter(
        queryset=AvailabilityChoice.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label='',
        empty_label='Наличие'
    )
    brand = django_filters.ModelChoiceFilter(
        queryset=Brand.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label='',
        empty_label='Бренд'
    )
    special = django_filters.ModelChoiceFilter(
        queryset=Special.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label='',
        empty_label='Спецпредложение'
    )
    for_who = django_filters.ModelChoiceFilter(
        queryset=ForWho.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label='',
        empty_label='Кому'
    )
    shape = django_filters.ModelChoiceFilter(
        queryset=Shape.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label='',
        empty_label='Форма корпуса'
    )
    material = django_filters.ModelChoiceFilter(
        queryset=Material.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label='',
        empty_label='Материал корпуса'
    )

    class Meta:
        model = Watch
        fields = (
            'condition', 'availability', 'brand', 'special',
            'for_who', 'shape', 'material'
        )
