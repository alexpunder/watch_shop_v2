from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Watch
from .forms import ShortMainForm, ShortFeedbackForm, ExtendBuybackForm

EXCLUDE_FIELDS = (
    'id', 'title', 'is_on_main', 'condition', 'availability', 'special',
    'for_who', 'shape', 'price', 'reference', 'image', 'material'
)


def index_page_view(request):
    watches = Watch.objects.filter(
        is_on_main=True
    )
    if request.method == 'POST':
        form = ShortMainForm(request.POST)
        if form.is_valid():
            messages.success(
                request,
                message=(
                    'Заявка успешно отправлена!'
                    'В ближайшее время с Васм свяжется наш специалист.'
                )
            )
            return HttpResponseRedirect(
                request.META.get('HTTP_REFERER')
            )
        else:
            messages.warning(
                request,
                message=(
                    'Ошибка заполнения формы: '
                    f'{form.errors.as_text()}'
                )
            )
    else:
        form = ShortMainForm()

    return render(
        request,
        template_name='index.html',
        context={'watches': watches, 'form': form},
    )


def buyback_view_page(request):
    if request.method == 'POST':
        form = ExtendBuybackForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(
                request,
                message=(
                    'Обращение зарегистрировано и будет обработано '
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
        form = ExtendBuybackForm(initial=request.POST)

    return render(
        request,
        template_name='watches/buyback.html',
        context={'buyback_form': form}
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


def watches_valuation_page_view(request):
    return render(
        request,
        template_name='watches/valuation.html'
    )


def about_page_view(request):
    return render(
        request,
        template_name='pages/about.html'
    )


def contacts_page_view(request):
    if request.method == 'POST':
        form = ShortFeedbackForm(request.POST)
        if form.is_valid():
            messages.success(
                request,
                message=(
                    'Вашее сообщение успешно отправлено. '
                    'Благодарим за обратную связь!'
                )
            )
            return HttpResponseRedirect(
                request.META.get('HTTP_REFERER')
            )
        else:
            messages.warning(
                request,
                message=(
                    'Ошибка заполнения формы: '
                    f'{form.errors.as_text()}'
                )
            )
    else:
        form = ShortFeedbackForm()

    return render(
        request,
        template_name='pages/contacts.html',
        context={'form': form}
    )


def faq_page_view(request):
    return render(
        request,
        template_name='pages/faq.html'
    )


def confidential_page_view(request):
    return render(
        request,
        template_name='pages/confidential.html'
    )


def terms_page_view(request):
    return render(
        request,
        template_name='pages/terms.html'
    )


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def server_error(request):
    return render(
        request, 'pages/500.html', status=500)
