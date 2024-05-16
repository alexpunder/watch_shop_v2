from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import ShortForm, CallForm, WatchRequestForm
from main.tasks import send_message
from watches.constants import DT_FORMAT


def footer_form_view(request):
    form = ShortForm()

    if request.method == 'POST':
        form = ShortForm(request.POST)
        if form.is_valid():
            data = form.save()
            send_message(
                'МАЛАЯ/НИЖНЯЯ ФОРМЫ',
                data.pub_date.strftime(DT_FORMAT), data.id
            )

            messages.success(
                request,
                message='Успешно.'
            )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(
                request,
                message=(
                    'Возникла ошибка заполнения формы: '
                    f'{form.errors.as_text()}'
                )
            )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def index_page_short_form(request):
    form = ShortForm()

    if request.method == 'POST':
        form = ShortForm(request.POST)
        if form.is_valid():
            data = form.save()
            send_message(
                'МАЛАЯ/НИЖНЯЯ ФОРМЫ',
                data.pub_date.strftime(DT_FORMAT), data.id
            )

            messages.success(
                request,
                message='Успешно.'
            )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(
                request,
                message=(
                    'Возникла ошибка заполнения формы: '
                    f'{form.errors.as_text()}'
                )
            )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def call_form_view(request):
    form = CallForm()

    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            data = form.save()
            send_message(
                'ЗАПРОС НА ОБРАТНЫЙ ЗВОНОК',
                data.pub_date.strftime(DT_FORMAT), data.id
            )

            messages.success(
                request,
                message='Успешно.'
            )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(
                request,
                message=(
                    'Возникла ошибка заполнения формы: '
                    f'{form.errors.as_text()}'
                )
            )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def watch_request_form_view(request):
    form = WatchRequestForm()

    if request.method == 'POST':
        form = WatchRequestForm(request.POST)
        if form.is_valid():
            data = form.save()
            send_message(
                'ЗАПРОС НА ПРИОБРЕТЕНИЕ ЧАСОВ',
                data.pub_date.strftime(DT_FORMAT), data.id
            )

            messages.success(
                request,
                message='Заявка успешно отправлена.'
            )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(
                request,
                message=(
                    'Возникла ошибка заполнения формы: '
                    f'{form.errors.as_text()}'
                )
            )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
