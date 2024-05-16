from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Watch
from .tasks import send_message
from forms.models import BuybackImage, ValuationImage
from forms.forms import ExtendValuationForm, ExtendBuybackForm
from watches.constants import DT_FORMAT, MAX_WATCHES_ON_INDEX_PAGE

EXCLUDE_FIELDS = (
    'id', 'title', 'is_on_main', 'condition', 'availability', 'special',
    'for_who', 'shape', 'price', 'reference', 'image', 'material'
)


def index_page_view(request):
    watches = Watch.objects.filter(
        is_on_main=True
    )[:MAX_WATCHES_ON_INDEX_PAGE]

    return render(
        request,
        template_name='index.html',
        context={'watches': watches},
    )


def buyback_view_page(request):
    if request.method == 'POST':
        form = ExtendBuybackForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save()
            send_message(
                'ВЫКУП ЧАСОВ', data.pub_date.strftime(DT_FORMAT), data.id
            )

            for file in request.FILES.getlist('buyback_images'):
                BuybackImage.objects.create(buyback=data, image=file)

            messages.success(
                request,
                message=(
                    'Обращение по ВЫКУПУ зарегистрировано и будет обработано '
                    'в ближайшее время.'
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
        context={'buyback_form': form}
    )


def watches_valuation_page_view(request):
    form = ExtendValuationForm()

    if request.method == 'POST':
        form = ExtendValuationForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save()
            send_message(
                'ОЦЕНКА ЧАСОВ', data.pub_date.strftime(DT_FORMAT), data.id
            )

            for file in request.FILES.getlist('valuation_images'):
                ValuationImage.objects.create(valuation=data, image=file)

            messages.success(
                request,
                message=(
                    'Обращение по ОЦЕНКЕ зарегистрировано и будет обработано '
                    'в ближайшее время.'
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
        context={'valuation_form': form}
    )


def watches_page_view(request):
    watches = Watch.objects.all()
    return render(
        request,
        template_name='watches/watches.html',
        context={'watches': watches}
    )


def watches_details_page_view(request, watch_id):
    watch = get_object_or_404(Watch, id=watch_id)
    data = {}

    for field in watch._meta.fields:
        if field.name not in EXCLUDE_FIELDS:
            verbose_name = field.verbose_name
            field_name = field.name
            value = getattr(watch, field_name)
            if value is not None:
                data[verbose_name] = value

    return render(
        request,
        template_name='watches/watches_details.html',
        context={'watch': watch, 'data': data.items()}
    )
