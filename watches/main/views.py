from django.contrib import messages
from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from forms.forms import ExtendBuybackForm, ExtendValuationForm
from forms.models import BuybackImage, ValuationImage
from watches.constants import (DESCRIPTIONS_DATA, DT_FORMAT,
                               MAX_WATCHES_ON_INDEX_PAGE,
                               MAX_WATCHES_ON_WATCHES_PAGE, TITLES_DATA)

from .filters import SearchFilter, WatchesFilter
from .models import Watch
from .tasks import send_message

EXCLUDE_FIELDS = (
    'id', 'title', 'is_on_main', 'condition', 'availability', 'special',
    'for_who', 'shape', 'price', 'reference', 'image', 'material',
    'convertation',
)


def search_view(request):
    watches = SearchFilter(
        request.GET,
        queryset=Watch.objects.select_related('convertation')
    )
    return render(
        request,
        template_name='watches/search_watches.html',
        context={
            'watches': watches,
            'title': TITLES_DATA.get('search'),
            'description': DESCRIPTIONS_DATA.get('search')
        }
    )


def index_page_view(request):
    watches = Watch.objects.filter(
        is_on_main=True
    ).select_related(
        'convertation'
    )[:MAX_WATCHES_ON_INDEX_PAGE]

    return render(
        request,
        template_name='index.html',
        context={
            'watches': watches,
            'title': TITLES_DATA.get('index'),
            'description': DESCRIPTIONS_DATA.get('index')
        },
    )


def buyback_view_page(request):
    if request.method == 'POST':
        form = ExtendBuybackForm(request.POST, request.FILES)
        if form.is_valid():
            with transaction.atomic():
                data = form.save()
                send_message.delay(
                    'ВЫКУП ЧАСОВ', data.pub_date.strftime(DT_FORMAT), data.id
                )

                for file in request.FILES.getlist('buyback_images'):
                    BuybackImage.objects.create(buyback=data, image=file)

                messages.success(
                    request,
                    message=(
                        'Обращение по ВЫКУПУ зарегистрировано и будет '
                        'обработано в ближайшее время.'
                    )
                )
                return HttpResponseRedirect(
                    request.META.get('HTTP_REFERER')
                )
        else:
            messages.error(
                request,
                message=(
                    'Ошибка заполнения формы: '
                    f'{form.errors.as_text()}'
                )
            )
    else:
        form = ExtendBuybackForm()

    return render(
        request,
        template_name='watches/buyback.html',
        context={
            'buyback_form': form,
            'title': TITLES_DATA.get('buyback'),
            'description': DESCRIPTIONS_DATA.get('buyback')
        }
    )


def watches_valuation_page_view(request):
    form = ExtendValuationForm()

    if request.method == 'POST':
        form = ExtendValuationForm(request.POST, request.FILES)
        if form.is_valid():
            with transaction.atomic():
                data = form.save()
                send_message.delay(
                    'ОЦЕНКА ЧАСОВ', data.pub_date.strftime(DT_FORMAT), data.id
                )

                for file in request.FILES.getlist('valuation_images'):
                    ValuationImage.objects.create(valuation=data, image=file)

                messages.success(
                    request,
                    message=(
                        'Обращение по ОЦЕНКЕ зарегистрировано и будет '
                        'обработано в ближайшее время.'
                    )
                )
                return HttpResponseRedirect(
                    request.META.get('HTTP_REFERER')
                )
        else:
            messages.error(
                request,
                message=(
                    'Ошибка заполнения формы: '
                    f'{form.errors.as_text()}'
                )
            )

    return render(
        request,
        template_name='watches/valuation.html',
        context={
            'valuation_form': form,
            'title': TITLES_DATA.get('valuation'),
            'description': DESCRIPTIONS_DATA.get('valuation')
        }
    )


def watches_page_view(request):
    watches_filter = WatchesFilter(
        request.GET, queryset=Watch.objects.select_related('convertation')
    )
    paginator = Paginator(
        watches_filter.qs,
        per_page=MAX_WATCHES_ON_WATCHES_PAGE
    )
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        template_name='watches/watches.html',
        context={
            'page_obj': page_obj,
            'filters': watches_filter,
            'title': TITLES_DATA.get('watches'),
            'description': DESCRIPTIONS_DATA.get('watches')
        }
    )


def watches_details_page_view(request, watch_id):
    watch = get_object_or_404(
        Watch.objects.select_related('convertation'),
        id=watch_id
    )
    data = {}

    for field in watch._meta.fields:
        if field.name not in EXCLUDE_FIELDS:
            verbose_name = field.verbose_name
            field_name = field.name
            value = getattr(watch, field_name)
            if value is not None:
                data[verbose_name] = value

    title = (
        f'{watch.brand.title} {watch.title} {watch.reference} '
        'купить швейцарские часы в часовом бутике YellowWatch'
    )
    description = (
        f'Купить {watch.brand.title} {watch.title} {watch.reference}'
    )

    return render(
        request,
        template_name='watches/watches_details.html',
        context={
            'watch': watch,
            'data': data.items(),
            'title': title,
            'description': description
        }
    )
